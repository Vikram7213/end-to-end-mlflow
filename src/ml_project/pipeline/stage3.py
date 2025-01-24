from ml_project.components.transformation import DataToTransformation
from ml_project.config.configuaration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        transform = ConfigurationManager()
        transform_config = transform.get_transform_conf()
        change = DataToTransformation(conf=transform_config)
        change.split_data()

        

