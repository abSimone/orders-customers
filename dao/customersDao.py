from utility.db import MySql

class CustomersDao:
    
    @classmethod
    def findAllCustomers(cls):
        MySql.openConnection()
        MySql.query("SELECT customerName FROM customers")
        results = MySql.getResults()
        MySql.closeConnection()
        return results
        # Questo è un test per la 
        # notifica