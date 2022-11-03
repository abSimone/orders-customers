from dao.customersDao import CustomersDao

class Customers:
    def __init__(self, customerName):
        self.customerName = customerName
        
class CustomersDto:
    @classmethod
    def getCustomers(cls):
        customers = []
        results = CustomersDao.findAllCustomers()
        for result in results:
            customer = Customers(result[0])
            customers.append({"customerName": customer.customerName})
        return customers