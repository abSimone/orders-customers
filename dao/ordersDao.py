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
