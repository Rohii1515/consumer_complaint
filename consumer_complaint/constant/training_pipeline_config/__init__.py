import os

PIPELINE_NAME = "consumer-complaint"
PIPELINE_ARTIFACT_DIR = os.path.join(os.getcwd(), "consumer_artifact")

from consumer_complaint.constant.training_pipeline_config.data_ingestion import *
from consumer_complaint.constant.training_pipeline_config.data_validation import *
from consumer_complaint.constant.training_pipeline_config.data_transformation import *
from consumer_complaint.constant.training_pipeline_config.model_trainer import *
from consumer_complaint.constant.training_pipeline_config.model_evaluation import *
from consumer_complaint.constant.training_pipeline_config.model_pusher import *
