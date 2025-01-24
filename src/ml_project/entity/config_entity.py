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
    

