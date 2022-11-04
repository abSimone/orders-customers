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

@app.get("/articles/status")
async def showArticleStatus(productCode : str):
    return Services().findArticleStatusService(productCode)

@app.get("/orders/fullDetails")
async def showFullDetails():
    return Services().findAllOrderDetailsService()

@app.get("/orders/articlesNumber")
async def showAllOrdersArticlesNumber(orderNumber : int | None = None):
    if orderNumber:
        return Services().findArticlesNumberByOrderNumberService(orderNumber)
    return Services().findAllOrdersArticlesNumberService()

@app.get("articles/orderedNumber")
async def showOrderedArticles(productCode : str | None = None):
    if productCode:
        return Services().findQuantityOrderedByArticleService(productCode)
    return Services().findAllArticlesQuantityOrderedService()

@app.get("articles/earnings")
async def showArticleEarnings(productCode : str | None = None):
    if productCode:
        return Services().findTotalEarningsByArticleService(productCode)
    return Services().findAllArticlesTotalEarningsService()

@app.get("orders/earnings")
async def showOrdersEarnings(orderNumber : int | None = None):
    if orderNumber:
        return Services().findTotalEarningsByOrderService(orderNumber)
    return Services().findAllOrdersTotalEarningsService()