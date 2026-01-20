from src.basic_project import logger
from src.basic_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.basic_project.pipeline.data_validation_pipeline import DataValidationTriningPipeline
from src.basic_project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.basic_project.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline




STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>> stage {STAGE_NAME} complted <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation=DataValidationTriningPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Date transformtion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transforamtion=DataTransformationTrainingPipeline()
    data_transforamtion.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e