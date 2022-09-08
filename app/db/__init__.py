from app.db.config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import models

engine = create_engine(DATABASE_URI)


Session = sessionmaker(bind=engine)


def init_db():
    # models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)


def get_session():
    with Session() as session:
        yield session
