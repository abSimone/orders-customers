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