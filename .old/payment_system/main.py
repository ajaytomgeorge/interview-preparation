from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from payment_system import Database

app = FastAPI(title="Payment Gateway")

class Transaction(BaseModel):
    amount:float

@app.middleware("http")
async def block_private_range(request:Request,call_next):
    client_host = request.client.host
    print(client_host)
    if client_host == '127.0.1.1':
        return JSONResponse(status_code=400, content={"detail":"blocked"})
    
    return await call_next(request)

@app.get("/{id}")
def get_transaction(id:int)->float:
    return Database.get_transaction(id)

@app.post("/{id}")
def post_transaction(id:int, transaction:Transaction, request:Request):
    if Database().insert_transaction(id,transaction.amount):
        return True

@app.get("/ip/")
def post_transaction( id:int, request:Request, )->str:
    return request.client.host