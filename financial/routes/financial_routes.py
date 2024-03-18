from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/financial", tags=["financial"])

class FinancialDataResponse(BaseModel):
    id: int
    description: str
    value: float
    type: str


class FinancialDataRequest(BaseModel):
    description: str
    value: float
    type: str



@router.get("/", response_model=List[FinancialDataResponse])
def list_counts():
    return [
        FinancialDataResponse(id = 1, description = "Salary", value = 1000.00, type = "income"),
        FinancialDataResponse(id = 2, description = "Salary", value = 1300.00, type = "outcome"),
    ]

@router.post("/", response_model=FinancialDataResponse, status_code=201)
def create_count(account: FinancialDataRequest):
    return FinancialDataResponse(id = 3, description = account.description, value = account.value, type = account.type)
    