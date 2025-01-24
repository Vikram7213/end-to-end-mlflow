from ml_project import logger
from ml_project.pipeline.stage1 import IngestionPipeline
from ml_project.pipeline.stage2 import DataValidationPipeline
stage = 'ingestion'
try:
    logger.info(f'the stage {stage} has started')
    ob = IngestionPipeline()
    ob.main()
    logger.info(f'the state {stage} execution is completed')
except Exception as e:
    raise e

stage = 'validation'
try:
    logger.info(f'the stage {stage} has started')
    q = DataValidationPipeline()
    q.main()
    logger.info(f'the stage {stage} has been completed!!')

except Exception as e:
    raise e