from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngest:
    root:Path
    source:str
    zipdir:Path
    unzipdir:Path

@dataclass(frozen=True)
class DataValid:
    rootdir:Path
    unzipdir:Path
    statusfile:str
    schema:dict
    
@dataclass(frozen=True)
class DataTransform:
    rootdir: Path
    data: Path

@dataclass(frozen=True)
class ModelTrain:
    rootdir:Path
    train:Path
    test:Path
    name:str
    alpha:float
    l1_ratio: float
    target:str

