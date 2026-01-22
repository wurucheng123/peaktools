import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL, NOTSET

def set_logging_level(level: str='ERROR'):
    """Set the logging level based on the provided string.

    :param str level: The logging level as a string. Options are 'CRITICAL', 'FATAL', 'ERROR', 'WARNING', 'WARN', 'INFO', 'DEBUG', or 'NOTSET'.
    """
    level = level.upper()
    
    logging.basicConfig(level=eval(level))

    logging.info(f"set logging level = {level}")