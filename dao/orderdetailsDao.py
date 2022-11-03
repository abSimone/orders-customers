from utility.db import MySql

class OrderDetails:

    @classmethod
    def getAllOrdersDetails(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT *\
                    FROM orderdetails
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data