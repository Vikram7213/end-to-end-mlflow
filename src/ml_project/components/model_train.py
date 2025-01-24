from ml_project.entity.config_entity import ModelTrain
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
import os

class ModelToTrainer:
    def __init__(self, conf:ModelTrain):
        self.config = conf

    def train(self):
        train_df = pd.read_csv(self.config.train)
        test_df = pd.read_csv(self.config.test)

        train_x = train_df.drop([self.config.target], axis=1)
        test_x = test_df.drop([self.config.target], axis=1)
        train_y=train_df[self.config.target]
        test_y=test_df[self.config.target]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=21)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.rootdir, self.config.name))
