from datetime import datetime
from pydantic import BaseModel


class createArea(BaseModel):
    name: str
    width: float
    height: float
    floorplan: str
    created_at: datetime


class createScanner(BaseModel):
    name: str
    x_pos: float
    y_pos: float
    area: int


class Node(BaseModel):
    id: int
    mac_address: str
    description: str


class Position(BaseModel):
    id: int
    area: int
    node: int
    x: float
    y: float
