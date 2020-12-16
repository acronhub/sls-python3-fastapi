import os
import logging
import logging.config
import pathlib


def create_logger():
    env = os.getenv("ENV", "local")

    # デバック
    current_dir = pathlib.Path(__file__).resolve().parent
    logging_conf_file = "{}/logging_{}.conf".format(current_dir, env)
    logging.config.fileConfig(logging_conf_file, disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    return logger
