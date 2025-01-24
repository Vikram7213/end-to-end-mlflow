import urllib.request
from ml_project import logger
import os
from ml_project.entity.config_entity import DataIngest
import zipfile

class DataToIngested:
    def __init__(self, config: DataIngest):
        self.config=config

    def download(self):
        if not os.path.exists(self.config.zipdir):
                fname, fhead = urllib.request.urlretrieve(
                     url=self.config.source,
                     filename=self.config.zipdir
                )
                logger.info(f'the file {fname} has been downloaded into {self.config.zipdir}')
        else:
             logger.info(f'unable to download the file')

    def extract(self):
         unzip_path = self.config.unzipdir
         os.makedirs(unzip_path, exist_ok=True)
         
         with zipfile.ZipFile(self.config.zipdir, 'r') as z:
              z.extractall(unzip_path)