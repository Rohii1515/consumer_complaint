from statistics import mode
from consumer_complaint.exception import ConsumerException
import sys
from consumer_complaint.logger import logger
from consumer_complaint.entity.config_entity import ModelPusherConfig
from consumer_complaint.entity.artifact_entity import ModelPusherArtifact, ModelTrainerArtifact
from pyspark.ml.pipeline import PipelineModel
from consumer_complaint.entity.estimator import S3FinanceEstimator
import os



class ModelPusher:

    def __init__(self, model_trainer_artifact: ModelTrainerArtifact, model_pusher_config: ModelPusherConfig):
        self.model_trainer_artifact = model_trainer_artifact
        self.model_pusher_config = model_pusher_config

    def push_model(self) -> str:
        try:
            model_registry = S3FinanceEstimator(bucket_name=self.model_pusher_config.bucket_name,s3_key=self.model_pusher_config.model_dir)
            model_file_path = self.model_trainer_artifact.model_trainer_ref_artifact.trained_model_file_path
            model_registry.save(model_dir=os.path.dirname(model_file_path),
                                key=self.model_pusher_config.model_dir
                                )
            # model = PipelineModel.load(self.model_trainer_artifact.model_trainer_ref_artifact.trained_model_file_path)
            # pushed_dir = self.model_pusher_config.model_dir
            # model.save(pushed_dir)
            return model_registry.get_latest_model_path()
        except Exception as e:
            raise ConsumerException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            pushed_dir = self.push_model()
            model_pusher_artifact = ModelPusherArtifact(model_pushed_dir=pushed_dir)
            logger.info(f"Model pusher artifact: {model_pusher_artifact}")
            return model_pusher_artifact
        except Exception as e:
            raise ConsumerException(e, sys)
