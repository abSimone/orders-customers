from utility.db import MySql

class CustomerDao:
    
    @classmethod
    def findAllCustomers(cls):
        MySql.openConnection()
        MySql.query("SELECT customerName FROM customers")
        results = MySql.getResults()
        MySql.closeConnection()
        return results
    
    @classmethod    
    def findCustomersByNumber(cls, customerNumber):
        MySql.openConnection()
        MySql.query(
            f"SELECT customerName \
            FROM customers \
            WHERE customerNumber = {customerNumber}"
        )
        results = MySql.getResults()
        MySql.closeConnection()
        return results