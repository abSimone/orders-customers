from dto.customerDto import CustomerDto
from dto.paymentsDto import PaymentDto
from dto.employeesDto import EmployeesDTO

from fastapi import APIRouter
from fastapi import FastAPI

router = APIRouter()
app = FastAPI()

@router.get("/customer")
def get_all_customer():
    return {"customer": CustomerDto.getCustomers()}

@router.get("/customer/{customerNumber}")
def get_customer_by_number(customerNumber: int):
    return {"customer": CustomerDto.getCustomersByNumber(customerNumber)}

@router.get("/payment")
def get_all_payment():
    return {"payment": PaymentDto.getPayments()}

@router.get("/payment/{amountValue}")
def get_payment_by_amount(amountValue: int):
    return {"payment": PaymentDto.getAmountOther(amountValue)}

@router.get("/payment/num/{paymentNumber}")
def get_num_payments_by_number(paymentNumber: int):
    return {"payment": PaymentDto.getNumPaymentsByNumber(paymentNumber)}

@app.get("/all-employees")
def get_all_employees():
    return {"all-employee": EmployeesDTO.getAllEmployees()}

@app.get("/id-employees/{employeeNumber}")
def get_id_employees(employeeNumber: int):
    return {"id-employee": EmployeesDTO.getEmployeesById(employeeNumber)}

@app.get("/city-employees/{id}")
def get_city_employees(id: int):
    return {"city-employee": EmployeesDTO.getEmployeesByCity(id)}