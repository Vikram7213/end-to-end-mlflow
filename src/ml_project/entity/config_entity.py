from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngest:
    root:Path
    source:str
    zipdir:Path
    unzipdir:Path