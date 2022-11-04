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
                     SELECT orderNumber, status\
                     FROM orders\
                     WHERE orderNumber = {orderNumber}
                     """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getArticlesStatus(cls, productCode):
        MySql.openConnection()
        MySql.query(f"""
                     SELECT o.orderNumber, o.status , od.productCode\
                     FROM orders o, orderdetails od\
                     WHERE od.orderNumber = o.orderNumber and od.productCode = '{productCode}'
                     """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data
