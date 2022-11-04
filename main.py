from fastapi import FastAPI
from services.dataServices import Services

app = FastAPI()

@app.get("/orders/all")
async def showAllOrders():
    return Services().findAllOrdersService()

@app.get("/orders/status")
async def showOrderStatus(orderNumber : int | None = None):
    if orderNumber:
        return Services().findOrderStatusService(orderNumber)
    return Services().findAllOrderStatusService()

@app.get("/articles/status/{productCode}")
async def showArticleStatus(productCode : str):
    return Services().findArticleStatusService(productCode)

@app.get("/orders/fullDetails")
async def showFullDetails():
    return Services().findAllOrderDetailsService()

@app.get("/orders/articlesNumber")
async def showAllOrdersArticlesNumber():
    return Services().findAllOrdersArticlesNumberService()