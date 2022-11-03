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
    def findAllTextDescriptions(cls, productCode):
        MySql.openConnection()
        MySql.query(
            f"SELECT textDescription  FROM productlines  WHERE productLine = '{productCode}'")

        data = MySql.getResults()
        MySql.closeConnection()
        return data
