from dao.employeesDao import EmployeesDAO

class Employees:
    def __init__(self, employeeNumber):
        self.employeeNumber = employeeNumber

class EmployeesDTO:
    @classmethod
    def getAllEmployees(cls):
        data = EmployeesDAO.findAllEmployees()
        newList = []
        for lista in data:
            newList.append(Employees(lista[0]))
        return newList

    @classmethod
    def getEmployeesById (cls, employeeNumber: int):
        data = EmployeesDAO.findEmployeesById(employeeNumber)
        newList = []
        for lista in data:
            newList.append(Employees(lista[0]))
        return newList
		
    @classmethod
    def getEmployeesByCity (cls, id: int):
        data = EmployeesDAO.findEmployeesByCity(id)
        newList = []
        for lista in data:
            newList.append(Employees(lista[0]))
        return newList