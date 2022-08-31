from sqlalchemy import create_engine

from ble_rtls_worker.db.config import DATABASE_URI
from ble_rtls_worker.models.models import Base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)


Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
