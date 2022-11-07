from fastapi import FastAPI 
from services.dataServices import Services

app = FastAPI()

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
