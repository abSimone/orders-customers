from utility.db import MySql


class PaymentDao:
    
    @classmethod
    def findAllPayments(cls):
        MySql.openConnection()
        MySql.query("SELECT customerNumber FROM payments")
        results = MySql.getResults()
        MySql.closeConnection()
        return results
    
    @classmethod
    def findAmountOtherValue(cls, value):
        MySql.openConnection()
        MySql.query(
            f"SELECT amount, customerName \
            FROM payments p, customers c \
            WHERE p.customerNumber = c.customerNumber \
            AND p.amount > {value} \
            Order by p.amount ASC"
        )
        results = MySql.getResults()
        MySql.closeConnection()     
        return results
    
    @classmethod
    def findNumPaymentsByNumber(cls, customerNumber):
        MySql.openConnection()
        MySql.query(
            f"SELECT customers.customerName, count(payments.customerNumber) \
            FROM customers \
            INNER JOIN payments \
            ON customers.customerNumber = payments.customerNumber \
            WHERE customers.customerNumber = {customerNumber}"
        )
        results = MySql.getResults()
        MySql.closeConnection()
        return results