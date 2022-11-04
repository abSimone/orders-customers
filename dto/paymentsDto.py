from dao.paymentDao import PaymentDao

class Payments:
    def __init__(self, customerNumber):
        self.customerNumber = customerNumber
        
        
class PaymentDto:
    
    @classmethod
    def getPayments(cls):
        customers = []
        results = PaymentDao.findAllPayments()
        for result in results:
            customer = Payments(result[0])
            customers.append({"customerNumber": customer.customerNumber})
        return customers
    
    @classmethod
    def getAmountOther(cls, value: int):
        customers = []
        results = PaymentDao.findAmountOtherValue(value)
        for result in results:
            customer = Payments(result[0])
            customers.append({"amount": customer.customerNumber})
        return customers
    
    @classmethod
    def getNumPaymentsByNumber(cls, customerNumber: int):
        results = PaymentDao.findNumPaymentsByNumber(customerNumber)
        newList = []
        for i in results:
            newList.append(i[0])
        return newList