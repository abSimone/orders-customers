from utility.db import MySql


class PaymentsDao:
    
    @classmethod
    def findAllPayments(cls):
        MySql.openConnection()
        MySql.query("SELECT customerNumber FROM payments")
        results = MySql.getResults()
        MySql.closeConnection()
        return results