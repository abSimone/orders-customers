from dao.officesDao import officeDAO

class Offices:
    def __init__(self, cityoffice = ""):
        self.office = cityoffice
       
class EmployeeNyc:
    def __init__(self, firstName = "", lastName = "", city = ""):
        self.firstname = firstName
        self.lastName = lastName
        self.city = city
      
class codeOffices:
    def __init__(self, codeoffice = ""):
        self.office = codeoffice

class OfficeDTO:
    @classmethod
    def getAllOffices(cls):
        data = officeDAO.findAllOffices()
        newList = []
        for lista in data:
            newList.append(Offices(lista[0].capitalize()))
        return newList

    @classmethod
    def getAllOfficesByCode(cls,code_office:int):
        data = officeDAO.findAllOfficesByCode(code_office)
        newList = []
        for lista in data:
            newList.append(Offices(lista[0]))
        return newList


    @classmethod
    def getAllEmployeeOfficeNyc(cls):
        data = officeDAO.findAllEmployeeOfficeNyc()
        newList = []
        for lista in data:
            newList.append(EmployeeNyc(lista[0],lista[1],lista[2]))
        return newList

test = officeDAO()
test.findAllEmployeeOfficeNyc()



