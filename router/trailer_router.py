from fastapi import APIRouter, Response ##Dividir Rutas
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.trailer_schema import TrailerSchema
from config.db import engine
from model.trailer_model import trailers
from typing import List
import json

trailer = APIRouter()

# @trailer.get("/")
# def root():
#     return "Hi I Am Trucks Route"

@trailer.get("/api/trailer")
def get_trailers():
    with engine.connect() as conn:
        result = conn.execute(trailers.select()).fetchall()
        conn.commit()
        return json.dumps(result, default=str)


@trailer.get("/api/trailer/{trailer_id}")
def get_trailer(trailer_id: int):
    with engine.connect() as conn:
        result = conn.execute(trailers.select().where(trailers.c.id == trailer_id)).first()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }
    

@trailer.post("/api/trailer", status_code=HTTP_201_CREATED)
def create_trailer(data_trailer: TrailerSchema):
    with engine.connect() as conn:
        new_trailer = data_trailer.model_dump()
        conn.execute(trailers.insert().values(new_trailer))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)


@trailer.put("/api/trailer/{trailer_id}")
def update_trailer(data_update: TrailerSchema, trailer_id: int):
    with engine.connect() as conn:
        conn.execute(trailers.update().values(trailer_type=data_update.trailer_type, number_plate=data_update.number_plate, capacity=data_update.capacity, status=data_update.status, cargo_type = data_update.cargo_type).where(trailers.c.id == trailer_id))
        conn.commit()

        result = conn.execute(trailers.select().where(trailers.c.id == trailer_id)).first()

        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }
    
@trailer.delete("/api/trailer/{trailer_id}", status_code=HTTP_204_NO_CONTENT)
def delete_trailer(trailer_id: int):
    with engine.connect() as conn:
        conn.execute(trailers.delete().where(trailers.c.id == trailer_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)

    