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

    @classmethod
    def getNumberOfArticles(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT orderNumber, count(*) as ArticlesNumber\
                    FROM classicmodels.orderdetails\
                    GROUP BY orderNumber;
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getNumberOfArticlesByOrderNumber(cls, orderNumber):
        MySql.openConnection()
        MySql.query(f"""
                    SELECT orderNumber, count(*) as ArticlesNumber\
                    FROM orderdetails\
                    WHERE orderNumber = '{orderNumber}'
                    GROUP BY orderNumber;
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllArticlesQuantityOrdered(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT productCode, sum(quantityOrdered)\
                    FROM orderdetails\
                    GROUP BY productCode;
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getQuantityOrderedByArticle(cls, productCode):
        MySql.openConnection()
        MySql.query(f"""
                    SELECT productCode, sum(quantityOrdered)\
                    FROM orderdetails\
                    WHERE productCode = {productCode}
                    GROUP BY productCode;
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllArticlesTotalEarnings(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT productCode, priceEach*sum(quantityOrdered)\
                    FROM orderdetails\
                    GROUP BY productCode;
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getTotalEarningsByArticle(cls, productCode):
        MySql.openConnection()
        MySql.query(f"""
                    SELECT productCode, priceEach*sum(quantityOrdered)\
                    FROM orderdetails\
                    WHERE productCode = {productCode}
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllOrdersTotalEarnings(cls):
        MySql.openConnection()
        MySql.query("""
                    SELECT orderNumber, sum(TotalEarnings)\
                    FROM (SELECT orderNumber, priceEach*sum(quantityOrdered) as TotalEarnings FROM orderdetails GROUP BY productCode) articleEarnings\
                    GROUP BY orderNumber
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getTotalEarningsByOrder(cls, orderNumber):
        MySql.openConnection()
        MySql.query(f"""
                    SELECT orderNumber, sum(TotalEarnings)\
                    FROM (SELECT orderNumber, priceEach*sum(quantityOrdered) as TotalEarnings FROM orderdetails GROUP BY productCode) articleEarnings\
                    WHERE orderNumber = {orderNumber}
                    """)
        data = MySql.getResults()
        MySql.closeConnection()

        return data