
from fastapi import FastAPI 
from services.dataServices import Services

app = FastAPI()


@app.get("/orders/all")
async def showAllOrders():
    return Services().findAllOrdersService()

@app.get("/orders/fullDetails")
async def showFullDetails():
    return Services().findAllOrderDetailsService()

@app.get("/orders/{query_id_orders}")
async def read_query_id_orders(query_id_orders : str, orderNumber : int | None = None):
    if query_id_orders == "status":
        if orderNumber:
            return Services().findOrderStatusService(orderNumber)
        return Services().findAllOrderStatusService()
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
async def read_query_id_articles(query_id_articles : str, productCode : str | None = None):
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


@app.get("/products/all")
async def showAllProducts():
    return Services().findAllProducts()

@app.get("/products/{query_id}")
async def read_query_id(query_id :str, productCode :str):
    if query_id == "productName":
            return Services().findProductName(productCode)    
    elif query_id =="quantityInStock":
        return Services().findQuantityInStock(productCode)    
    elif query_id == "buyPrice":
        return Services().findBuyPrice(productCode) 
    elif query_id == "productLine":
        return Services().findProductLine(productCode) 

@app.get("/customer")
async def get_all_customer():
    return Services().findAllCustomers()

@app.get("/customer/{customerNumber}")
async def get_customer_by_number(customerNumber: int):
    return Services().findCustomerByNumber(customerNumber)

@app.get("/payment")
async def get_all_payment():
    return Services().findAllPayments()

@app.get("/payment/{amountValue}")
async def get_payment_by_amount(amountValue: int):
    return Services().findPaymentByAmount(amountValue)

@app.get("/payment/num/{paymentNumber}")
async def get_num_payments_by_number(paymentNumber: int):
    return Services().findNumPaymentsByNumber(paymentNumber)

@app.get("/all-employees")
async def get_all_employees():
    return Services().findAllEmployees()

@app.get("/id-employees/{employeeNumber}")
async def get_id_employees(employeeNumber: int):
    return Services().findEmployeesById(employeeNumber)

@app.get("/city-employees/{id}")
async def get_city_employees(id: int):
    return Services().findEmployeesByCity(id)

@app.get("/all-offices")
async def get_all_offices():
    return Services().findAllOffices()

@app.get("/code-offices/{code}")
async def get_code_offices(code: int):
    return Services().findOfficesByCode(code)

@app.get("/employees-office")
async def get_employees_office():
    return Services().findEmployeesByOffice()
