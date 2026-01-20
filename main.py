from src.basic_project import logger
from src.basic_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.basic_project.pipeline.data_validation_pipeline import DataValidationTriningPipeline





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