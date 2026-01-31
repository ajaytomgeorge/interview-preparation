import time
from collections import deque
from datetime import datetime , timedelta
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="RateLimiterTest")
MAX_REQUESTS = 5
SLIDING_WINDOW = 15


class RateLimiter():
    """RateLimits requests from user based on ip"""
    def __init__(self):
        self.memory:dict[str,deque] = {}
    def update_queue(self,ip):
        ip_info = self.memory[ip].copy()
        for val in ip_info:
            current_time = datetime.now()
            if current_time - val > timedelta(seconds=SLIDING_WINDOW):
                print("popped",self.memory[ip].pop())             

    def  allow(self,ip):
        if not ip in self.memory:
            self.memory[ip] = deque()
        if len(self.memory[ip]) > MAX_REQUESTS:
            self.update_queue(ip)
            if len(self.memory[ip]) > MAX_REQUESTS:
                return False
        self.memory[ip].append(datetime.now())
        print("Added entry to queue",ip, datetime.now() )
        return  True
        
rate_limiter = RateLimiter()

class Ip(BaseModel):
    ip:str

@app.post("/mypost")
def my_root(ip:Ip)->str:
    if rate_limiter.allow(ip.ip):
        return "Success"
    return "Limit execeed"

