from config import Config
from services.transaction_processor import TransactionProcessor
from services.vertex_service import VertexAIService
from utils.logger import setup_logging


def main():
    # Load configuration
    try:
        config = Config.from_yaml()
    except FileNotFoundError:
        print("Config file not found, using default configuration")
        raise

    # Setup logging
    logger = setup_logging(config)
    logger.info("Starting processing script")

    try:
        # Initialize services
        vertex_service = VertexAIService(config)
        processor = TransactionProcessor(config, vertex_service)

        # Load dataset
        with open(config.processing.dataset_path, "r") as f:
            dataset = f.read().splitlines()
        dataset = [d for d in dataset if len(d) > 0]
        logger.info(f"Loaded {len(dataset)} prompts")

        # Process transactions
        success_count, failure_count = processor.process_batch(dataset)
        # Log results
        logger.info(f"Finished {success_count} prompts")
        logger.info(f"Failed {failure_count} prompts")
        logger.info("Processing completed successfully")

    except Exception as e:
        logger.error(f"Script failed with error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
