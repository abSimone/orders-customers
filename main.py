from fastapi import FastAPI
from services.dataServices import Services

app = FastAPI()

@app.get("/orders/{query_id_orders}")
async def read_query_id_orders(query_id_orders : str, orderNumber : int | None = None):
    if query_id_orders == "all":
        return Services().findAllOrdersService()
    elif query_id_orders == "status":
        if orderNumber:
            return Services().findOrderStatusService(orderNumber)
        return Services().findAllOrderStatusService()
    elif query_id_orders == "fullDetails":
        return Services().findAllOrderDetailsService()
    elif query_id_orders == "articlesNumber":
        if orderNumber:
            return Services().findArticlesNumberByOrderNumberService(orderNumber)
        return Services().findAllOrdersArticlesNumberService()
    elif query_id_orders == "totalEarnings":
        if orderNumber:
            return Services().findTotalEarningsByOrderService(orderNumber)
        return Services().findAllOrdersTotalEarningsService()


@app.get("/articles/status")
async def showArticleStatus(productCode : str):
    return Services().findArticleStatusService(productCode)

@app.get("/articles/{query_id_articles}")
async def read_query_id_articles(query_id_articles : str, productCode : str):
    if query_id_articles == "totalEarnings":
        if productCode:
            return Services().findTotalEarningsByArticleService(productCode)
        return Services().findAllArticlesTotalEarningsService()
    elif query_id_articles == "quantityOrdered":
        if productCode:
            return Services().findQuantityOrderedByArticleService(productCode)
        return Services().findAllArticlesQuantityOrderedService()


@app.get("/productlines/info")
async def showProductLines(productLine : str | None = None):
    if productLine:
        return Services().getDescriptionService(productLine)
    return Services().getAllProductLinesService()


@app.get("/products/{query_id}")
async def read_query_id(query_id :str, productCode :str):
    if query_id == "all":
        return Services().findAllProducts(productCode)
    elif query_id == "productName":
            return Services().findProductName(productCode)    
    elif query_id =="quantityInStock":
        return Services().findQuantityInStock(productCode)    
    elif query_id == "buyPrice":
        return Services().findBuyPrice(productCode) 
    elif query_id == "productLine":
        return Services().findProductLine(productCode) 