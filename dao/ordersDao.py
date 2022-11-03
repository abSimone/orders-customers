from utility.db import MySql

class Order:

    @classmethod
    def getAllOrders(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT *\
                    FROM orders
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getOrderStatusByOrderNumber(cls, orderNumber):
        MySql.openConnection()
        MySql.query(f"""
                     SELECT *\
                     FROM orders\
                     WHERE orderNumber = {orderNumber}
                     """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllInfosByProductCode(cls, orderNumber):
        MySql.openConnection()
        MySql.query(f"""
                     SELECT o.*, od.productCode, od.quantityOrdered, od.priceEach, od.orderLineNumber\
                     FROM orders o, orderdetails od\
                     WHERE o.orderNumber = {orderNumber} and od.orderNumber = o.orderNumber
                     """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data
