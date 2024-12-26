import logging
import os
from datetime import datetime


def setup_logging(config):
    if not os.path.exists(config.logging.log_dir):
        os.makedirs(config.logging.log_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(config.logging.log_dir, f"process_{timestamp}.log")

    level = getattr(logging, config.logging.level.upper())

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
    return logging.getLogger(__name__)
