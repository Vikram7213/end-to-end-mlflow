from ml_project.config.configuaration import ConfigurationManager
from ml_project.components.ingestion import DataToIngested
from ml_project import logger

stage = 'data ingestion'

class IngestionPipeline:
    def __init__(self):
        pass

    def main(self):    
    
        configuaration = ConfigurationManager()
        ingest_config = configuaration.get_ingestion_conf()
        data_ingestion = DataToIngested(config=ingest_config)
        data_ingestion.download()
        data_ingestion.extract()
