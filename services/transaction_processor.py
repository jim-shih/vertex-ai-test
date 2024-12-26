import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from tqdm import tqdm


class TransactionProcessor:
    def __init__(self, config, vertex_service):
        self.config = config.processing
        self.prompt_template = config.prompts.transaction_template
        self.vertex_service = vertex_service
        self.logger = logging.getLogger(__name__)

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(self.config.output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generate timestamped output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(self.config.output_file)
        name, ext = os.path.splitext(filename)
        self.output_file = os.path.join(output_dir, f"output_{timestamp}{ext}")

    def process_transaction(self, transaction_name):
        try:
            prompt = self.prompt_template.format(transaction_name)
            self.logger.debug(f"Processing transaction: {transaction_name}")

            response = self.vertex_service.generate_content(prompt).text

            replacing_word = ["```json", "```", "```json\n", "```", "{", "}", '"', "`", "\n"]
            for word in replacing_word:
                response = response.replace(word, "")

            with open(self.output_file, "a+") as f:
                output_string = f"transaction_name: {transaction_name}, Response: {response}\n"
                f.write(output_string)

            self.logger.debug(f"Successfully processed transaction: {transaction_name}")
            return True
        except Exception as e:
            with open(self.output_file, "a+") as f:
                output_string = f"transaction_name: {transaction_name}, Response: Error.\n"
                f.write(output_string)
            self.logger.error(f"Error processing {transaction_name}: {str(e)}")
            return False

    def process_batch(self, dataset):
        success_count = 0
        failure_count = 0

        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            future_to_name = {
                executor.submit(self.process_transaction, name): name for name in dataset
            }

            with tqdm(total=len(dataset)) as pbar:
                for future in as_completed(future_to_name):
                    name = future_to_name[future]
                    try:
                        if future.result():
                            success_count += 1
                        else:
                            failure_count += 1
                    except Exception as e:
                        self.logger.error(f"Task for {name} generated an exception: {str(e)}")
                        failure_count += 1
                    pbar.update(1)

        return success_count, failure_count
