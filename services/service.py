from dto.customerDto import CustomerDto
from dto.paymentsDto import PaymentDto
from fastapi import APIRouter

router = APIRouter()

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
