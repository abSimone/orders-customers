from dao.officesDao import officeDAO

class Offices:
    def __init__(self, title):
        self.title = title
      


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
    def getAllEmployeeByCode(cls):
        data = officeDAO.findAllEmployeeByCode()
        newList = []
        for lista in data:
            newList.append(Offices(lista[0]))
            return newList




