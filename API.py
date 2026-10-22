from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

# Request Body: is the API equilivent to a struct in c++ , it declares the shape  
class Transactions (BaseModel):
    description: str | None = None# this makes the choice of adding a description of the transaction optional 
    price: float
    date: date 
    category: str 

stored_transaction = {} # this is how we're going to store the transactions to be able to output them whenever 

tran_id = 0 

app = FastAPI()

@app.post("/Transactions/")
async def create_transaction(new_transaction: Transactions):
   # This is called In-Memory Storage: wiped whenever server restarts
    global tran_id # lets this function change the counter defined outside it
    transaction_dict = new_transaction.model_dump()
    tran_id += 1 # increments everytime to generate new id number
    stored_transaction[tran_id] = transaction_dict
    returned_transaction = {"id": tran_id, **transaction_dict} #  ** unpacks the fields into the response next to the id
    return returned_transaction


@app.get("/Transactions") # defines the route for GET 
def get_transactions(): # this func gives us all transactions 
    return stored_transaction


@app.get("/Transactions/{tran_id}")
def single_transaction(tran_id: int):
    if tran_id not in stored_transaction:  # checks if id is there 
        raise HTTPException(status_code=404, detail = "Item not found") # displays error code for the user 
    
    return stored_transaction[tran_id]
    
