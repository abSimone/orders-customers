from dto.ordersDto import OrderDto
from dto.orderdetailsDto import OrderDetailsDto
from dto.productlinesDto import productLinesDto
from dto.productsDto import ProductDto
from dto.customerDto import CustomerDto
from dto.paymentsDto import PaymentDto
from dto.employeesDto import EmployeesDTO
from dto.officesDto import OfficeDTO

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

    
    @classmethod
    def findAllCustomers(cls):
        return CustomerDto.getCustomers()
    
    @classmethod
    def findCustomerByNumber(cls, customerNumber):
        return CustomerDto.getCustomersByNumber(customerNumber)
    
    @classmethod
    def findAllPayments(cls):
        return PaymentDto.getPayments()
    
    @classmethod
    def findPaymentByAmount(cls, amountValue):
        return PaymentDto.getAmountOther(amountValue)
    
    @classmethod
    def findNumPaymentsByNumber(cls, paymentNumber):
        return PaymentDto.getNumPaymentsByNumber(paymentNumber)
    
    @classmethod
    def findAllEmployees(cls):
        return EmployeesDTO.getAllEmployees()
    
    @classmethod
    def findEmployeesById(cls, employeeNumber):
        return EmployeesDTO.getEmployeesById(employeeNumber)
    
    @classmethod
    def findEmployeesByCity(cls, id):
        return EmployeesDTO.getEmployeesByCity(id)
    
    @classmethod
    def findAllOffices(cls):
        return OfficeDTO.getAllOffices()
    
    @classmethod
    def findOfficesByCode(cls, code):
        return OfficeDTO.getAllOfficesByCode(code)
    
    @classmethod
    def findEmployeesByOffice(cls):
        return OfficeDTO.getAllEmployeeOfficeNyc()
