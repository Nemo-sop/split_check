from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, List
from pathlib import Path
from Friendship_conserver import Friendship_conserver  # Import your class

app = FastAPI()

class ExpensesRequest(BaseModel):
    guest_expensess: Dict[str, float]

class ExpensesResponse(BaseModel):
    total_spent: float
    individual_spent: float
    debts: Dict[str, float]
    transfers: List[str]

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    # Serve the HTML file
    html_path = Path("index.html")  # Ensure index.html is in the same directory as main.py
    if not html_path.exists():
        return HTMLResponse("<h1>index.html file not found</h1>", status_code=404)
    return HTMLResponse(content=html_path.read_text(), status_code=200)


@app.post("/calculate", response_model=ExpensesResponse)
def calculate_expenses(request: ExpensesRequest):
    guest_expensess = request.guest_expensess
    if not guest_expensess:
        raise HTTPException(status_code=400, detail="Invalid input")

    # Use the Friendship_conserver class
    divider = Friendship_conserver()
    divider.divide_expensess(guest_expensess)
    divider.balance(guest_expensess)
    transfers = divider.calculate_transfers()

    return ExpensesResponse(
        total_spent=divider.total_spent,
        individual_spent=divider.individual_spent,
        debts=divider.debts,
        transfers=transfers
    )
