from fastapi import FastAPI
import services.service as service 

app = FastAPI()

app.include_router(service.router)

