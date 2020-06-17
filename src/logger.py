import logging
import os
from logging.handlers import RotatingFileHandler
import pathlib

log = logging.getLogger(__name__)

import logging
logFormatter = logging.Formatter("%(asctime)s [%(module)s/%(funcName)s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileName = "example"
logPath = pathlib.Path(__file__).parent.absolute()
fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

logging.getLogger("discord").setLevel(logging.WARNING)
rootLogger.setLevel(level=logging.INFO)
