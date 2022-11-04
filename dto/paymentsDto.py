from dao.paymentDao import PaymentDao

class Payments:
    def __init__(self, customerNumber = None, customerName = None):
        self.customerNumber = customerNumber
        self.customerName = customerName

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
            newList.append(Payments(i[0], i[1]))
        return newList
