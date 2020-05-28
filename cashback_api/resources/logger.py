import logging
from os import getenv

logging.basicConfig(level=logging.DEBUG,
                    filename=getenv("LOG_PATH") or "logs/cashback.log",
                    filemode='w+',
                    format='%(name)s - %(levelname)s - %(message)s')


def log_info(message: str):
    logging.info(message)


def log_warning(message: str):
    logging.warning(message)


def log_error(message: str):
    logging.error(message)
