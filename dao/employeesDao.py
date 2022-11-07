from utility.db import MySql

class EmployeesDAO:

  @classmethod
  def findAllEmployees(cls):
    MySql.openConnection()
    MySql.query(
      "SELECT employeeNumber \
       FROM employees"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    return data

  @classmethod
  def findEmployeesById(cls, employeeNumber):
    MySql.openConnection()
    MySql.query(
      f"SELECT firstName, lastName\
      FROM employees\
      WHERE employeeNumber = {employeeNumber}"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    return data
		
  @classmethod
  def findEmployeesByCity(cls, officeCode):
    MySql.openConnection()
    MySql.query(
      f"SELECT firstName, email, city \
      FROM employees as Emp \
      JOIN offices as Off ON Emp.officeCode = Off.officeCode \
      WHERE Off.officeCode > {officeCode}"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    return data