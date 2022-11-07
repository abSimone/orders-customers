from dto.officesDto import OfficeDTO

from fastapi import FastAPI

app = FastAPI()

@app.get("/office")
async def get_all_office():
    return {"office": OfficeDTO.getAllOffices()}


@app.get("/codeoffice/{code_office}")
def getAllOfficesByCode(code_office: int):
    return {"office code": OfficeDTO.getAllOfficesByCode(code_office)}


@app.get("/nyc-employee-office/")
def getAllEmployeeOfficeNyc():
    return {"office": OfficeDTO.getAllEmployeeOfficeNyc()}