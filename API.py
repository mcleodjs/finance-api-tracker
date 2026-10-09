from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

# Request Body: is the API equilivent to a struct in c++ , it declares the shape  
class Transactions (BaseModel):
    description: str | None = None# this makes the choice of adding a date of the transaction optional 
    price: float
    date: date 
    category: str 

Stored_transaction = {}

tran_id = 0 

app = FastAPI()

@app.post("/Transactions/")
async def create_transaction(new_transaction: Transactions):
   # This is called In-Memory Storage
    global tran_id 
    transaction_dict = new_transaction.model_dump()
    tran_id += 1 
    Stored_transaction[tran_id] = transaction_dict
    returned_transaction = {"id": tran_id, **transaction_dict}
    
    
    return returned_transaction