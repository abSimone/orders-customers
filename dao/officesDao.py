from utility.db import MySql

class officesDAO:

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
    