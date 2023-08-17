from fastapi import APIRouter, Response ##Dividir Rutas
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.truck_schema import TruckSchema
from config.db import engine
from model.truck_model import trucks
from typing import List
import json

truck = APIRouter()


@truck.get("/api/truck")
def get_trucks():
    with engine.connect() as conn:
        result = conn.execute(trucks.select()).fetchall()
        conn.commit()
        # return json.dumps(result, default=str)
        return {
            "success": True,
            "data": json.dumps(result, default=str),
            "message": HTTP_204_NO_CONTENT
        }


@truck.get("/api/truck/{truck_id}")
def get_truck(truck_id: int):
    with engine.connect() as conn:
        result = conn.execute(trucks.select().where(trucks.c.id == truck_id)).first()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }
    

@truck.post("/api/truck", status_code=HTTP_201_CREATED)
def create_truck(data_truck: TruckSchema):
    with engine.connect() as conn:
        new_truck = data_truck.model_dump()
        conn.execute(trucks.insert().values(new_truck))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)


@truck.put("/api/user/{truck_id}")
def update_truck(data_update: TruckSchema, truck_id: int):
    with engine.connect() as conn:
        conn.execute(trucks.update().values(model=data_update.model, number_plate=data_update.number_plate, capacity=data_update.capacity, status=data_update.status).where(trucks.c.id == truck_id))
        conn.commit()

        result = conn.execute(trucks.select().where(trucks.c.id == truck_id)).first()

        # return {
        #     "success": True,
        #     "data": json.dumps(result, default=str)
        # }
        return Response(status_code=HTTP_204_NO_CONTENT)
    
@truck.delete("/api/truck/{truck_id}", status_code=HTTP_204_NO_CONTENT)
def delete_truck(truck_id: int):
    with engine.connect() as conn:
        conn.execute(trucks.delete().where(trucks.c.id == truck_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)

    