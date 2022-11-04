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
  def findAllEmployeeByCode(cls):
    MySql.openConnection()
    MySql.query(
        f"SELECT firstName, lastName, officeCode \
        FROM employees\
        WHERE officeCode IN (1 , 2, 3)\
        ORDER BY officeCode"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    print (data)
    return data
