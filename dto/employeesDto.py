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