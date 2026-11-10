from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
# Request Body: is the API equilivent to a struct in c++ , it declares the shape  
class Transactions (BaseModel):
    description: str | None = None# this makes the choice of adding a description of the transaction optional 
    price: float = Field(gt=0) # insures value is greater than 0 
    date: date 
    category: str = Field(min_length=1)

stored_transaction = {} # this is how we're going to store the transactions to be able to output them whenever 

tran_id = 0 

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"])
# CREATE portion of CRUD endpoints 
@app.post("/Transactions")
async def create_transaction(new_transaction: Transactions):
   # This is called In-Memory Storage: wiped whenever server restarts
    global tran_id # lets this function change the counter defined outside it
    transaction_dict = new_transaction.model_dump()
    tran_id += 1 # increments everytime to generate new id number
    stored_transaction[tran_id] = transaction_dict
    returned_transaction = {"id": tran_id, **transaction_dict} #  ** unpacks the fields into the response next to the id
    return returned_transaction

# # READ portion of CRUD endpoints 
@app.get("/Transactions") # defines the route for GET 
def get_transactions(): # this func gives us all transactions 
    all_transactions =[]
    for id, info in stored_transaction.items():
        all_transactions.append({"id": id, **info})
    
    return all_transactions
 
@app.get("/Transactions/{tran_id}")
def single_transaction(tran_id: int):
    if tran_id not in stored_transaction:  # checks if id is there 
        raise HTTPException(status_code=404, detail = "Item not found") # displays error code for the user 
    
    return {"id":tran_id, **stored_transaction[tran_id]}

# DELTE portion of CRUD endpoints 
@app.delete("/Transactions")
def remove_transactions(tran_id: int):
    if tran_id not in stored_transaction:
        raise HTTPException(status_code=404, detail= "Cant be found") 
    del stored_transaction[tran_id]

    return{"deleted": tran_id}
# UPDATE portion of CRUD id
@app.put("/Transactions/{tran_id}")
def update_transaction(tran_id: int, updated_transaction: Transactions ):
    # Checks if the id even exists
    if tran_id not in stored_transaction:
        raise HTTPException(status_code=404, detail = "Item not found")
    
    stored_transaction[tran_id] = updated_transaction.model_dump() #Updates Transaction 

    return {"message": "Transactions updated","id": stored_transaction[tran_id]}
