import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(message)s')

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def log(self, message):
        self.logger.info(message)
