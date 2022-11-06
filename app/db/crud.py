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


def get_positions(db: Session):
    positions = db.query(models.Position).all()
    return positions


def get_latest_position_for_node(db: Session, node_id: int):
    position = (
        db.query(models.Position)
        .filter_by(node=node_id)
        .order_by(models.Position.id.desc())
        .first()
    )
    return position


def clear_positions(db: Session):
    db_positions = db.query(models.Position)
    db_positions.delete()
    db.commit()


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


def update_area(area: schemas.AreaUpdate, area_id: int, db: Session):
    db_area = db.get(models.Area, area_id)
    area_data = area.dict(exclude_unset=True)

    for key, value in area_data.items():
        setattr(db_area, key, value)
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def get_areas(db: Session):
    areas = db.query(models.Area).all()
    return areas


def get_area_by_id(area_id: int, db: Session):
    print(area_id)
    db_area = db.get(models.Area, area_id)
    return db_area


def delete_area(db: Session, area_id: str):
    db_area = db.query(models.Area).filter_by(id=area_id)
    db_area.delete()
    db.commit()


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
    return {
        scanner.name: {
            "id": scanner.id,
            "name": scanner.name,
            "x": scanner.x_pos,
            "y": scanner.y_pos,
            "area": scanner.area,
        }
        for scanner in scanners
    }


def get_scanners_by_area(area_id: int, db: Session):
    scanners = db.query(models.Scanner).filter(models.Scanner.area == area_id).all()
    return scanners


def update_scanner(scanner: schemas.ScannerUpdate, scanner_id: int, db: Session):
    db_scanner = db.get(models.Scanner, scanner_id)
    scanner_data = scanner.dict(exclude_unset=True)
    print(scanner_data)
    print(scanner_id)
    for key, value in scanner_data.items():
        setattr(db_scanner, key, value)
    db.add(db_scanner)
    db.commit()
    db.refresh(db_scanner)
    return db_scanner


def create_node(db: Session, node: schemas.Node):
    db_node = models.Node(mac_address=node.mac_address, description=node.description)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node


def delete_node(db: Session, mac_address: str):
    db_node = db.query(models.Node).filter_by(mac_address=mac_address)
    db_node.delete()
    db.commit()


def clear_nodes(db: Session):
    db_nodes = db.query(models.Node)
    db_nodes.delete()
    db.commit()


def get_nodes(db: Session):
    nodes = db.query(models.Node).all()
    return nodes
