from ml_project.constants import *
from ml_project.utils.com import read_yml, create_dir
from ml_project.entity.config_entity import DataIngest
from ml_project.entity.config_entity import DataValid
from ml_project.entity.config_entity import DataTransform

class ConfigurationManager:
    def __init__(
            self,
            conf = CONFIG_PATH,
            sche = SCHEMA_PATH,
            param = PARAMS_PATH):
        self.conf = read_yml(conf)
        self.sche = read_yml(sche)
        self.param = read_yml(param)

        create_dir([self.conf.artifact_root])

    def get_ingestion_conf(self) -> DataIngest:
        config = self.conf.data_ingestion

        create_dir([config.rootdir])

        data_ingest_config = DataIngest(
            root=config.rootdir,
            source=config.url,
            zipdir=config.localdir,
            unzipdir=config.unzipdir
        )

        return data_ingest_config
    
    def get_validation_conf(self) -> DataValid:
        config = self.conf.data_validation
        schema = self.sche.COLUMNS
        create_dir([config.rootdir])

        validate_config = DataValid(
            rootdir=config.rootdir,
            unzipdir=config.unzipdir,
            statusfile=config.status,
            schema=schema
        )

        return validate_config
    
    def get_transform_conf(self)->DataTransform:
        config = self.conf.data_transformation
        create_dir([config.rootdir])

        transform_config = DataTransform(
            rootdir=config.rootdir,
            data=config.data
        )

        return transform_config
    

    