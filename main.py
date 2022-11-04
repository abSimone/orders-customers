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

@app.get("/productlines/all")
async def showAllProductLines():
    return Services().getAllProductLinesService()

@app.get("/productlines/description/{productLine}")
async def showProductLinesDescription(productLine : str):
    return Services().getAllDescriptionService(productLine)

@app.get("/products/all")
async def showAllProducts():
    return Services().findAllProducts()

@app.get("/products/productName/")
async def showProductName(productCode : str):
    return Services().findProductName(productCode)    

@app.get("/products/quantityInStock/")
async def showQuantityInStock(productCode : str):
    return Services().findQuantityInStock(productCode)       

@app.get("/products/buyPrice/")
async def showBuyPrice(productCode : str):
    return Services().findBuyPrice(productCode)  

@app.get("/product/productLine/")
async def showProductLine(productCode : str):
    return Services().findProductLine(productCode)              


 