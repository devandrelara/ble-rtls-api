from typing import List
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

from app.db import Session, get_session, init_db
from app.db.models import models
from app.db import crud
from app.schemas import schemas

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/area")
def get_areas(session: Session = Depends(get_session)):
    return crud.get_areas(db=session)


@app.get("/area/{aread_id}")
def get_area(area_id: int, session: Session = Depends(get_session)):
    return crud.get_area_by_id(area_id=area_id, db=session)


@app.post("/area/", response_model=schemas.Area)
def create_area(area: schemas.Area, session: Session = Depends(get_session)):
    return crud.create_area(db=session, area=area)


@app.patch("/area/{area_id}")
def update_area(
    area_update: schemas.AreaUpdate,
    area_id: int,
    session: Session = Depends(get_session),
):
    return crud.update_area(area=area_update, area_id=area_id, db=session)


@app.delete("/area/{area_id}", status_code=204)
def delete_area(area_id: int, session: Session = Depends(get_session)):
    return crud.delete_area(area_id=area_id, db=session)


@app.get("/scanner")
def get_scanners(session: Session = Depends(get_session)):
    return crud.get_scanners(db=session)


@app.get("/scanner/area/{area_id}")
def get_scanners_by_area(area_id: int, session: Session = Depends(get_session)):
    return crud.get_scanners_by_area(area_id=area_id, db=session)


@app.patch("/scanner/{scanner_id}")
def update_scanner(
    scanner_upadte: schemas.ScannerUpdate,
    scanner_id: int,
    session: Session = Depends(get_session),
):
    return crud.update_scanner(
        scanner=scanner_upadte, scanner_id=scanner_id, db=session
    )


@app.post("/scanner/", response_model=schemas.Scanner)
def create_scanner(scanner: schemas.Scanner, session: Session = Depends(get_session)):
    return crud.create_scanner(db=session, scanner=scanner)


@app.get("/node")
def get_nodes(session: Session = Depends(get_session)):
    return crud.get_nodes(db=session)


@app.post("/node/", response_model=schemas.Node)
def create_node(node: schemas.Node, session: Session = Depends(get_session)):
    return crud.create_node(db=session, node=node)


@app.delete("/node/", status_code=204)
def clear_nodes(session: Session = Depends(get_session)):
    return crud.clear_nodes(db=session)


@app.delete("/node/{mac_address}", status_code=204)
def delete_node(mac_address: str, session: Session = Depends(get_session)):
    return crud.delete_node(mac_address=mac_address, db=session)


@app.get("/position/")
def get_positions(session: Session = Depends(get_session)):
    return crud.get_positions(db=session)


@app.get("/position/latest/{node_id}")
def get_node_latest_position(node_id: int, session: Session = Depends(get_session)):
    return crud.get_latest_position_for_node(db=session, node_id=node_id)


@app.post("/position/", response_model=schemas.Position)
def save_position(position: schemas.Position, session: Session = Depends(get_session)):
    return crud.save_position(db=session, position=position)


@app.delete("/position/", status_code=204)
def clear_positions(session: Session = Depends(get_session)):
    return crud.clear_positions(db=session)


@app.get(
    "/area/img/{area_name}",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
)
def get_image_by_name(area_name: str):

    image = open(f"images/{area_name}.png", "rb")
    f = image.read()
    return Response(content=f, media_type="image/png")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
