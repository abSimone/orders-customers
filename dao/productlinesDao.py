from utility.db import MySql


class ProductsLines:
    @classmethod
    def findAllProductLines(cls):
        MySql.openConnection()
        MySql.query(
            "SELECT * FROM productlines"
            )


        data = MySql.getResults()
        MySql.closeConnection()
        return data


    @classmethod
    def findSpecificProductLine(cls, productLine):
        MySql.openConnection()
        MySql.query(
            f"SELECT productLine, textDescription  FROM productlines  WHERE productLine = '{productLine}'")

        data = MySql.getResults()
        MySql.closeConnection()
        return data
