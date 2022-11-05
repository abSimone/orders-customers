from fastapi import FastAPI
import service 

app = FastAPI()

app.include_router(service.router)

