import logging


"""
Logging module.
Decorate functions to log their
execution process in a file.
"""


logging.basicConfig(filename="sample.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


def log_this_function(function):
    def wrapper(*args, **kwargs):
        logging.info("------------------------Start-session------------------------")
        logging.info(f"Enter {function.__name__} function.")
        logging.info(f"Try executing {function.__name__} function.")
        try:
            result = function(*args, **kwargs)
            if type(result) is Exception:
                raise result
            logging.info(f"{function.__name__} function executed successfully!")
            return result
        except Exception as ex:
            logging.error(f"Error occurred while executing {function.__name__} function.")
            logging.error(f"Error: {ex}")
            return None
        finally:
            logging.info("-------------------------End-session-------------------------\n\n")
    return wrapper
