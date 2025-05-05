
from pydantic import BaseModel
from typing import Iterable 

class Unit(BaseModel):
    name: str
    symbol: str

class Units(Iterable):
    roots: list[Unit]