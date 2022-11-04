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
    def getProductName(cls, productCode):
            MySql.openConnection()
            MySql.query(f"""
                        SELECT productCode, productName\
                        FROM products\
                        WHERE productCode = {productCode}
                        """)
            data = MySql.getResults()
            MySql.closeConnection()

            return data
    
    @classmethod
    def getQuantityInStock(cls, productCode):
            MySql.openConnection()
            MySql.query(f"""
                        SELECT productCode, quantityInStock\
                        FROM products\
                        WHERE productCode = {productCode}
                        """)
            data = MySql.getResults()
            MySql.closeConnection()

            return data

    @classmethod
    def getBuyPrice(cls, productCode):
            MySql.openConnection()
            MySql.query(f"""
                        SELECT productCode, buyPrice\
                        FROM products\
                        WHERE productCode = {productCode}
                        """)
            data = MySql.getResults()
            MySql.closeConnection()

            return data
    
    @classmethod
    def getProductLine(cls, productCode):
            MySql.openConnection()
            MySql.query(f"""
                        SELECT productCode, productLine\
                        FROM products\
                        WHERE productCode = {productCode}
                        """)
            data = MySql.getResults()
            MySql.closeConnection()

            return data


    