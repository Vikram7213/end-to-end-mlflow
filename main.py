from ml_project import logger
from ml_project.pipeline.stage1 import IngestionPipeline
from ml_project.pipeline.stage2 import DataValidationPipeline
from ml_project.pipeline.stage3 import DataTransformationPipeline
from ml_project.pipeline.stage4 import ModelTrainingPipeline
from ml_project.pipeline.stage5 import EvaluationPipeline
import mlflow

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

stage = 'transformation'
try:
    logger.info(f'stage {stage} has started')
    w = DataTransformationPipeline()
    w.main()
    logger.info(f'the stage {stage} has been completed')

except Exception as e:
    raise e

stage = 'training'
try:
    logger.info(f'stage {stage} is started')

    e = ModelTrainingPipeline()
    e.main()
    
    logger.info(f'the stage {stage} is completed successfully!')

except Exception as e:
     raise e

stage = 'evaluation'
try:
    logger.info(f'stage {stage} has started')
    w = EvaluationPipeline()
    w.main()
    logger.info(f'the stage {stage} has been completed')

except Exception as e:
    raise e