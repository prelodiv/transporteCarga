# from fastapi import APIRouter, Response ##Dividir Rutas
# from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
# from schema.user_schema import UserSchema
# from config.db import engine
# from model.users import users
# from typing import List
# import json

# user = APIRouter()

# @user.get("/")
# def root():
#     return "Hi I Am FastApi Router"

# @user.get("/api/user")
# async def get_users():
#     with engine.connect() as conn:
#         result = conn.execute(users.select()).fetchall()
#         conn.commit()
#         return json.dumps(result, default=str)


# @user.get("/api/user/{user_id}")
# def get_user(user_id: int):
#     with engine.connect() as conn:
#         result = conn.execute(users.select().where(users.c.id == user_id)).first()
#         conn.commit()
#         return {
#             "success": True,
#             "data": json.dumps(result, default=str)
#         }
    

# @user.post("/api/user", status_code=HTTP_201_CREATED)
# def create_user(data_user: UserSchema):
#     with engine.connect() as conn:
#         new_user = data_user.model_dump()
#         new_user["user_passw"] = generate_password_hash(data_user.user_passw, "pbkdf2:sha256:30", 30)

#         print(new_user)

#         conn.execute(users.insert().values(new_user))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)


# @user.put("/api/user/{user_id}")
# def update_user(data_update: UserSchema, user_id: int):
#     with engine.connect() as conn:
#         encryp_passw = generate_password_hash(data_update.user_passw, "pbkdf2:sha256:30", 30)
#         conn.execute(users.update().values(name=data_update.name, shortname=data_update.shortname, user_passw=encryp_passw).where(users.c.id == user_id))
#         conn.commit()

#         result = conn.execute(users.select().where(users.c.id == user_id)).first()
#         print(result)

#         return {
#             "success": True,
#             "data": json.dumps(result, default=str)
#         }
    
# @user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
# def delete_user(user_id: int):
#     with engine.connect() as conn:
#         conn.execute(users.delete().where(users.c.id == user_id))
#         conn.commit()

#         return Response(status_code=HTTP_204_NO_CONTENT)

    
