from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Area(BaseModel):
    name: str
    width: float
    height: float
    floorplan: str

    class Config:
        orm_mode = True


class AreaUpdate(BaseModel):
    name: Optional[str]
    width: Optional[float]
    height: Optional[float]
    floorplan: Optional[str]

    class Config:
        orm_mode = True


class Scanner(BaseModel):
    name: str
    x_pos: float
    y_pos: float
    area: int

    class Config:
        orm_mode = True


class ScannerUpdate(BaseModel):
    name: Optional[str]
    x_pos: Optional[float]
    y_pos: Optional[float]
    area: Optional[int]

    class Config:
        orm_mode = True


class Node(BaseModel):
    mac_address: str
    description: str

    class Config:
        orm_mode = True


class Position(BaseModel):
    area: int
    node: int
    x: float
    y: float

    class Config:
        orm_mode = True
