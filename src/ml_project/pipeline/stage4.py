from ml_project.components.model_train import ModelToTrainer
from ml_project.config.configuaration import ConfigurationManager

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        con = ConfigurationManager()
        con_conf = con.get_model_conf()
        train = ModelToTrainer(conf=con_conf)
        train.train()