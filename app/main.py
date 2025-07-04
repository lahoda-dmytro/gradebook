from fastapi import FastAPI
from app.api import routes_root

app = FastAPI()
app.include_router(routes_root.router)

