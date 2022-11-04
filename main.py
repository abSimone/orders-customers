from fastapi import FastAPI
from services.dataServices import Services

app = FastAPI()

@app.get("/orders/all")
async def showAllOrders():
    return Services().findAllOrdersService()

@app.get("/orders/status/{orderNumber}")
async def showOrderStatus(orderNumber : int):
    return Services().findOrderStatusService(orderNumber)

@app.get("/articles/status/{productCode}")
async def showArticleStatus(productCode : str):
    return Services().findArticleStatusService(productCode)