from dao.officesDao import officesDAO

class Offices:
    def init(self, title):
        self.title = title


class OfficesDTO:
    @classmethod
    def getAllOffices(cls):
        data = officesDAO.findAllOffices()
        newList = []
        for lista in data:
            newList.append(Offices(lista[0].capitalize()))
        return newList



