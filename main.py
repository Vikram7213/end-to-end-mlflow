from ml_project import logger
from ml_project.pipeline.stage1 import IngestionPipeline

stage = 'ingestion'
try:
    logger.info(f'the stage {stage} has started')
    ob = IngestionPipeline()
    ob.main()
    logger.info(f'the state {stage} execution is comppleted')
except Exception as e:
    raise e