from fastapi import FastAPI, Depends 
from app.routers import auth_routes, order_routes


app = FastAPI()

app.include_router(
    auth_routes.auth_router
)
app.include_router(
    order_routes.order_router
)
