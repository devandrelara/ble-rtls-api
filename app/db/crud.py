from datetime import datetime
from app.db import Session
from app.db.models import models
from app.schemas import schemas


def save_position(db: Session, position: schemas.Position):
    db_position = models.Position(
        area=position.area, node=position.node, x=position.x, y=position.y
    )
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position


def create_area(db: Session, area: schemas.Area):
    db_area = models.Area(
        name=area.name,
        width=area.width,
        height=area.height,
        floorplan=area.floorplan,
        created_at=datetime.now(),
    )
    print(db_area)
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def get_areas(db: Session):
    areas = db.query(models.Area).all()
    return areas


def create_scanner(db: Session, scanner: schemas.Scanner):
    db_scanner = models.Scanner(
        name=scanner.name, x_pos=scanner.x_pos, y_pos=scanner.y_pos, area=scanner.area
    )
    db.add(db_scanner)
    db.commit()
    db.refresh(db_scanner)
    return db_scanner


def get_scanners(db: Session):
    scanners = db.query(models.Scanner).all()
    return scanners


def create_node(db: Session, node: schemas.Node):
    db_node = models.Node(mac_address=node.mac_address, description=node.description)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node


def get_nodes(db: Session):
    nodes = db.query(models.Node).all()
    return nodes
