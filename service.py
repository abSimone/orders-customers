from fastapi import FastAPI

from dto.employeesDto import EmployeesDTO

app = FastAPI()

@app.get("/all-employees")
def get_all_employees():
    return {"all-employee": EmployeesDTO.getAllEmployees()}

@app.get("/id-employees/{employeeNumber}")
def get_id_employees(employeeNumber: int):
    return {"id-employee": EmployeesDTO.getEmployeesById(employeeNumber)}

@app.get("/city-employees/{id}")
def get_city_employees(id: int):
    return {"city-employee": EmployeesDTO.getEmployeesByCity(id)}