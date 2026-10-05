from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

# Request Body: is the API equilivent to a struct in c++ , it declares the shape  
class Transactions (BaseModel):
    description: str | None = None# this makes the choice of adding a date of the transaction optional 
    price: float
    date: date 
    category: str 


app = FastAPI()

@app.post("/Transactions/")
async def Transaction(Transactions: Transactions):
    return Transactions