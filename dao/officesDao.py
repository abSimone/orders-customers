from utility.db import MySql

class officeDAO:

  @classmethod
  def findAllOffices(cls):
    MySql.openConnection()
    MySql.query(
      "SELECT city \
       FROM offices"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    return data
    

  @classmethod
  def findAllOfficesByCode(cls, code_office):
    MySql.openConnection()
    MySql.query(
       f"SELECT officeCode \
        FROM offices \
        WHERE officeCode ={code_office}"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    return data

  @classmethod
  def findAllEmployeeOfficeNyc(cls):
    MySql.openConnection()
    MySql.query(
        f"SELECT firstName, lastName, city \
        FROM offices o, employees e\
        WHERE o.officeCode = e.officeCode \
        AND city like 'NYC'"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    print(data)
    return data
