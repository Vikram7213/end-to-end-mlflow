from ml_project.config.configuaration import DataValid
import pandas as pd
class DataToValidated:
    def __init__(self, conf: DataValid):
        self.config = conf
        pass
    
    def get_datavalid_status(self):
        validstat = None
        
        data = pd.read_csv(self.config.unzipdir)
        cols = list(data.columns)

        req_cols = self.config.schema.keys()
        try:
            for _ in cols:    
                if _ not in req_cols:
                    validstat=False
                    with open(self.config.statusfile,'w') as a:
                        a.write(f'{validstat}')
                    
                else:
                    validstat=True
                    with open(self.config.statusfile,'w') as a:
                        a.write(f'{validstat}')

            return validstat
        
        except Exception as e:
            raise e
