from hate_speech_detection.logger import logging
from hate_speech_detection.exception import CustomException
import sys
from hate_speech_detection.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_to_gcloud("hate00332211", "data.zip", "data.zip")