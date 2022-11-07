from dao.customerDao import CustomerDao

class Customer:
    def __init__(self, customerName):
        self.customerName = customerName

class CustomerDto:
    
    @classmethod
    def getCustomers(cls):
        customers = []
        results = CustomerDao.findAllCustomers()
        for result in results:
            customer = Customer(result[0])
            customers.append({"customerName": customer.customerName})
        return customers
    
    @classmethod
    def getCustomersByNumber(cls, customerNumber: int):
        results = CustomerDao.findCustomersByNumber(customerNumber)
        newList = []
        for i in results:
            newList.append(i[0])
        return newList
