"""
    use frequently usable functions here along with the logging done
"""

import os
from box import ConfigBox
from box.exceptions import BoxValueError
from ml_project import logger as logg
from ensure import ensure_annotations
from pathlib import Path
import json
import yaml
from typing import Any
import joblib
import base64

@ensure_annotations
def read_yml(yaml_path:Path) -> ConfigBox:
    """Takes a .yml path as input and outputs a ConfigBox."""
    try:
        with open(yaml_path) as yml_file:
            con = yaml.safe_load(yml_file)
            logg.info(f'loaded the yaml file from {yml_file}')
            return ConfigBox(con)
    except(BoxValueError):
        raise ValueError('empty file!')
    except Exception as e:
        raise e

@ensure_annotations
def create_dir(path_to_dir: list, verbose = True):
    """Takes a list of paths and creates them and logs it"""
    for p in path_to_dir:
        os.makedirs(p, exist_ok=True)
        if verbose:
            logg.info(f'created the file {p}')

@ensure_annotations
def save_json(path_json:Path, data:dict):
    """saves the dictonary in the form of the json format"""
    with open(path_json, 'w') as f:
        json.dump(data, f, indent=4)
        logg.info(f'json file saved at {path_json}')

@ensure_annotations
def save_bin(path_saved:Path, data:Any):
    """saves the data into binary format in the path given"""
    joblib.dump(data, path_saved)
    logg.info(f'binary file saved at {path_saved}')

@ensure_annotations
def load_bin(path:Path) -> Any:
    """loads the binary file"""
    d = joblib.load(path)
    logg.info(f'loaded binary from file {path}')
    return d

@ensure_annotations
def get_size(path:Path) -> str:
    """gives out the size of contents in the path in terms of kb"""
    kb = round(os.path.getsize(path)/1024)
    return f'~ {kb} KB'

