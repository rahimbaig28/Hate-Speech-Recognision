from hate_speech_detection.logger import logging
from hate_speech_detection.exception import CustomException
import sys

try:
    a = 1/"0"
except Exception as e:
    raise CustomException(e, sys) from e

#logging.info("Creating empty file: demo.py")