from typing import List
import uvicorn
from fastapi import FastAPI, Depends
from app.db import Session, get_session, init_db
from app.db.models import models
from app.db import crud
from app.schemas import schemas

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def health_check():
    return "Alive!"


@app.get("/area")
def get_areas(session: Session = Depends(get_session)):
    return crud.get_areas(db=session)


@app.get("/node")
def get_nodes(session: Session = Depends(get_session)):
    return crud.get_nodes(db=session)


@app.get("/scanner")
def get_scanners(session: Session = Depends(get_session)):
    return crud.get_scanners(db=session)


@app.get("/position/")
def get_positions(session: Session = Depends(get_session)):
    return crud.get_positions(db=session)


@app.post("/position/", response_model=schemas.Position)
def save_position(position: schemas.Position, session: Session = Depends(get_session)):
    return crud.save_position(db=session, position=position)


@app.post("/area/", response_model=schemas.Area)
def create_area(area: schemas.Area, session: Session = Depends(get_session)):
    return crud.create_area(db=session, area=area)


@app.post("/node/", response_model=schemas.Node)
def create_node(node: schemas.Node, session: Session = Depends(get_session)):
    return crud.create_node(db=session, node=node)


@app.delete("/node/", status_code=204)
def clear_nodes(session: Session = Depends(get_session)):
    return crud.clear_nodes(db=session)


@app.delete("/node/{mac_address}", status_code=204)
def delete_node(mac_address: str, session: Session = Depends(get_session)):
    return crud.delete_node(mac_address=mac_address, db=session)


@app.post("/scanner/", response_model=schemas.Scanner)
def create_scanner(scanner: schemas.Scanner, session: Session = Depends(get_session)):
    return crud.create_scanner(db=session, scanner=scanner)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
