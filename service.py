from dto.customerDto import CustomerDto
from dto.paymentsDto import PaymentDto
from fastapi import FastAPI

from dto.officesDto import OfficeDTO

app = FastAPI()

@app.get("/customer")
def get_all_customer():
    return {"customer": CustomerDto.getCustomers()}

@app.get("/customer/{customerNumber}")
def get_customer_by_number(customerNumber: int):
    return {"customer": CustomerDto.getCustomersByNumber(customerNumber)}

@app.get("/payment")
def get_all_payment():
    return {"payment": PaymentDto.getPayments()}

@app.get("/payment/{amountValue}")
def get_payment_by_amount(amountValue: int):
    return {"payment": PaymentDto.getAmountOther(amountValue)}

@app.get("/payment/num/{paymentNumber}")
def get_num_payments_by_number(paymentNumber: int):
    return {"payment": PaymentDto.getNumPaymentsByNumber(paymentNumber)}
