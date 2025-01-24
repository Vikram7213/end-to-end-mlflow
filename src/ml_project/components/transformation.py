from ml_project.entity.config_entity import DataTransform
from sklearn.model_selection import train_test_split
import os
import pandas as pd
from ml_project import logger

class DataToTransformation:
    def __init__(self, conf: DataTransform):
        self.config = conf
    
    def split_data(self):
        data = pd.read_csv(self.config.data)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.rootdir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.rootdir, 'test.csv'), index=False)

        logger.info(f'split the data into train and the test')
        logger.info(f'the test data is {test.shape} shaped')
        logger.info(f'the train data is {train.shape} shaped')
