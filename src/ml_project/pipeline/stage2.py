from ml_project import logger
from ml_project.config.configuaration import ConfigurationManager
from ml_project.components.validation import DataToValidated

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):

        configuration = ConfigurationManager()
        valid_config = configuration.get_validation_conf()
        validating = DataToValidated(conf=valid_config)
        validating.get_datavalid_status()
