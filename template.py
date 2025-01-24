from pathlib import Path 
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

pro = 'ml_project'

lof = [
    '.github/workflows/.gitkeep',
    f'src/{pro}/__init__.py',
    f'src/{pro}/components/__init__.py',
    f'src/{pro}/utils/com.py',
    f'src/{pro}/utils/__init__.py',
    f'src/{pro}/config/configuaration.py',
    f'src/{pro}/config/__init__.py',
    f'src/{pro}/pipeline.py/__init__.py',
    f'src/{pro}/entity/__init__.py',
    f'src/{pro}/entity/config_entity.py',
    f'src/{pro}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'req.txt',
    'setup.py',
    'trails/t1.ipynb',
    'templates/index.html'
]

for f in lof:
    f = Path(f)
    fdir, fname = os.path.split(f)

    if fdir != '':
        os.makedirs(fdir,exist_ok=True)
        logging.info(f'creating the directory {fdir} for the {fname}')

    if (not os.path.exists(f)) or (os.path.getsize(f)==0):
        with open(f, 'w') as _:
            pass
            logging.info(f'creating empty file {f}')

    else:
        logging.info(f'the file already exist the file is {f}')
