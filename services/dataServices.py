from dto.ordersDto import OrderDto
from dto.orderdetailsDto import OrderDetailsDto

from dto.productlinesDto import productLinesDto

class Services:

    @classmethod
    def findAllOrdersService(cls):
        return OrderDto().findAllOrders()

    @classmethod
    def findOrderStatusService(cls, orderNumber : int):
        return OrderDto().findOrderStatus(orderNumber)

    @classmethod
    def findArticleStatusService(cls, orderNumber : int):
        return OrderDto().findArticleStatus(orderNumber)

    @classmethod
    def findAllOrderDetailsService(cls):
        return OrderDetailsDto().findAllOrderDetails()

    @classmethod
    def findAllOrdersArticlesNumberService(cls):
        return OrderDetailsDto().findAllOrdersArticlesNumber()

    @classmethod
    def findAllOrdersArticlesNumberByOrderNumberService(cls, orderNumber : int):
        return OrderDetailsDto().findAllOrdersArticlesNumberByOrderNumber(orderNumber)
    
    @classmethod
    def findAllArticlesQuantityOrderedService(cls):
        return OrderDetailsDto().findAllArticlesQuantityOrdered()

    @classmethod
    def findQuantityOrderedByArticleService(cls, productCode : str):
        return OrderDetailsDto().findQuantityOrderedByArticle(productCode)

    @classmethod
    def findAllArticlesTotalEarningsService(cls):
        return OrderDetailsDto().findAllArticlesTotalEarnings()

    @classmethod
    def findTotalEarningsByArticleService(cls, productCode : str):
        return OrderDetailsDto().findTotalEarningsByArticle(productCode)

    @classmethod
    def findAllOrdersTotalEarningsService(cls):
        return OrderDetailsDto().findAllOrdersTotalEarnings()

    @classmethod
    def findTotalEarningsByOrderService(cls, orderNumber : int):
        return OrderDetailsDto().findTotalEarningsByOrder(orderNumber)

    @classmethod
    def getAllProductLinesService(cls):
        return productLinesDto().getAllProductLines()

    @classmethod 
    def getAllDescriptionService(cls, productLine : str):
        return productLinesDto().getDescription(productLine)