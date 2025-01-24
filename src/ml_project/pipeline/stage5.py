from ml_project.components.evaluation import ModelToEvaluate
from ml_project.config.configuaration import ConfigurationManager

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        con = ConfigurationManager()
        conf = con.get_eval_conf()
        evaluate = ModelToEvaluate(conf=conf)
        evaluate.log_mlflow()