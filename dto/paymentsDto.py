from dao.paymentsDao import PaymentsDao

class Payments:
    def __init__(self, customerNumber):
        self.customerNumber = customerNumber
        
        
class CustomersDto:
    @classmethod
    def getPayments(cls):
        customers = []
        results = PaymentsDao.findAllPayments()
        for result in results:
            customer = Payments(result[0])
            customers.append({"customerNumber": customer.customerNumber})
        return customers