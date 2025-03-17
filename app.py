from fastapi import FastAPI
from pydantic import BaseModel
from service import TransferService
from models import Transaction

app = FastAPI()

class TransferRequest(BaseModel):
    source: str
    destination: str
    amount: float

@app.post("/transfer")
def transfer_money(request: TransferRequest):
    transaction = Transaction(request.source, request.destination, request.amount)
    return TransferService.transfer_funds(transaction)
