from datetime import datetime
from pydantic import BaseModel


class Area(BaseModel):
    name: str
    width: float
    height: float
    floorplan: str

    class Config:
        orm_mode = True


class Scanner(BaseModel):
    name: str
    x_pos: float
    y_pos: float
    area: int

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
