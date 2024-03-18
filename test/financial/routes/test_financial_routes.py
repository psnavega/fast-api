from fastapi.testclient import TestClient
from financial.routes.financial_routes import router

client = TestClient(router)

def test_should_list_financial_accounts_successfully():
    response = client.get("/financial")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "description": "Salary", "value": 1000.00, "type": "income"},
        {"id": 2, "description": "Salary", "value": 1300.00, "type": "outcome"},
    ]

def test_should_create_financial_account_successfully():
    new_account = {"description": "Salary", "value": 1000.00, "type": "income"}

    copy_account = new_account.copy()

    copy_account["id"] = 3

    response = client.post("/financial", json=new_account)
    assert response.status_code == 201
    assert response.json() == copy_account