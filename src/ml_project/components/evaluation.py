from ml_project.entity.config_entity import Evaluation
from sklearn.metrics import root_mean_squared_error, r2_score
import pandas as pd
import joblib
import mlflow
from pathlib import Path
from ml_project.utils.com import save_json

class ModelToEvaluate:
    def __init__(self, conf: Evaluation):
        self.config = conf

    def eval_metrics(self, actual, pred):
        rmse = root_mean_squared_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, r2
    
    def log_mlflow(self):

        test_d = pd.read_csv(self.config.test)
        model = joblib.load(self.config.model_path)

        x = test_d.drop([self.config.target_col], axis=1)
        y = test_d[[self.config.target_col]]
        
        with mlflow.start_run() as s:
            preds = model.predict(x)
            rmse, r2 = self.eval_metrics(y, preds)

            score = {'rmse': rmse, 'r2': r2}
            save_json(path_json=Path(self.config.metric_file), data=score)
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('rmse', rmse)
            mlflow.log_metric('r2 score', r2)

            mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet model")
