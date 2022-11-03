from utility.db import MySql

class Product:

    @classmethod
    def getAllProducts(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT *\
                    FROM products
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data


    

    @classmethod
    def getAllProductName(cls):
            MySql.openConnection()
            MySql.query("""
                    SELECT productName\
                    FROM products
                    """)
            data = MySql.getResults()
            MySql.closeConnection()

            return data

    


    