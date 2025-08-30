import logging


def set_up():
    logger = logging.getLogger("db_helper")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("my_app.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger