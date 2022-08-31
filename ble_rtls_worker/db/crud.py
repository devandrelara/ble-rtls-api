from datetime import datetime
from sqlalchemy import create_engine


from sqlalchemy.orm import sessionmaker

from ble_rtls_worker.db.config import DATABASE_URI
from ble_rtls_worker.db.models import models
from ble_rtls_worker.schemas import schemas

engine = create_engine(DATABASE_URI)


Session = sessionmaker(bind=engine)


def recreate_database():
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)


def create_area(db: Session, area: schemas.createArea):
    db_area = models.Area(
        name=area.name,
        width=area.width,
        height=area.height,
        floorplan=area.floorplan,
        created_at=datetime.now(),
    )
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def create_scanner(db: Session, scanner: schemas.createScanner):
    db_scanner = models.Scanner(
        name=scanner.name, x_pos=scanner.x_pos, y_pos=scanner.y_pos, area=scanner.area
    )
    db.add(db_scanner)
    db.commit()
    db.refresh(db_scanner)
    return db_scanner
