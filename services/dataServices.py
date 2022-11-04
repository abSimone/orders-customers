from dto.ordersDto import OrderDto
from dto.orderdetailsDto import OrderDetailsDto
from dto.productlinesDto import productLinesDto
from dto.productsDto import ProductDto

class Services:

    @classmethod
    def findAllOrdersService(cls):
        return OrderDto().findAllOrders()

    @classmethod
    def findOrderStatusService(cls, orderNumber : int):
        return OrderDto().findOrderStatus(orderNumber)

    @classmethod
    def findAllOrderStatusService(cls):
        return OrderDto().findAllOrderStatus()

    @classmethod
    def findArticleStatusService(cls, productCode : int):
        return OrderDto().findArticleStatus(productCode)

    @classmethod
    def findAllOrderDetailsService(cls):
        return OrderDetailsDto().findAllOrderDetails()

    @classmethod
    def findAllOrdersArticlesNumberService(cls):
        return OrderDetailsDto().findAllOrdersArticlesNumber()

    @classmethod
    def findArticlesNumberByOrderNumberService(cls, orderNumber : int):
        return OrderDetailsDto().findArticlesNumberByOrderNumber(orderNumber)
    
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
    def getDescriptionService(cls, productLine : str):
        return productLinesDto().getDescription(productLine)

    @classmethod
    def findAllProducts(cls):
        return ProductDto().findAllProducts()

    @classmethod
    def findProductName(cls, productCode : str):
        return ProductDto().findProductName(productCode)

    @classmethod
    def findQuantityInStock(cls, productCode : str):
        return ProductDto().findQuantityInStock(productCode)  

    @classmethod
    def findBuyPrice(cls, productCode : str):
        return ProductDto().findBuyPrice(productCode)    

    @classmethod
    def findProductLine(cls, productCode : str):
        return ProductDto().findProductLine(productCode)