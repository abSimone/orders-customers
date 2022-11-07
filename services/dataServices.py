from dto.customerDto import CustomerDto
from dto.paymentsDto import PaymentDto
from dto.employeesDto import EmployeesDTO
from dto.officesDto import OfficeDTO


class Services:
    
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