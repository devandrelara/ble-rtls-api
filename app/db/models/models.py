from operator import index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    UniqueConstraint,
    Float,
    Integer,
    String,
    Date,
    ForeignKey,
)

Base = declarative_base()


class Area(Base):
    __tablename__ = "areas"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    width = Column(Float)
    height = Column(Float)
    floorplan = Column(String)
    created_at = Column(Date)

    def __repr__(self):
        return "<Area(id='{}', width='{}', height='{}', floorplan={}, created_at={})>".format(
            self.id, self.width, self.height, self.floorplan, self.created_at
        )


class Scanner(Base):
    __tablename__ = "scanners"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    x_pos = Column(Float)
    y_pos = Column(Float)
    area = Column(Integer, ForeignKey("areas.id"))


class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True)
    mac_address = Column(String)
    description = Column(String)


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    area = Column(Integer, ForeignKey("areas.id"))
    node = Column(Integer, ForeignKey("nodes.id"))
    x = Column(Float)
    y = Column(Float)
