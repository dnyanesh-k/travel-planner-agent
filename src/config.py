from dotenv import load_dotenv
import logging

# load env variabless immediately
load_dotenv()

def setup_logging():
    """Sets up the global logging configuration once"""

    log_format = "%(asctime)s %(levelname)s - %(message)s"

    console_handler = logging.StreamHandler()

    file_handler = logging.FileHandler(
        "travel-planner.log", encoding='utf-8'
    )
    # create a logger
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[console_handler, file_handler]
    )
