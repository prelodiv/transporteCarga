from fastapi import FastAPI
#from router.router import user
from router.truck_router import truck
from router.trailer_router import trailer

app = FastAPI()

#app.include_router(user)
app.include_router(truck)
app.include_router(trailer)
