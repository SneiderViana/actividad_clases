from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hola():
    return {"HELLO FASTAPI"}

@app.get("/Isprime")
def Primo(numero): 
     for n in range(2,numero):
       if numero % n == 0:
          return False  
     return True

@app.get("/fibonnacci")
def fibonnacci(num: int):
     a=0
     b=1
     for n in range(0, num):
        c=a+b
        a=b
        b=c
     return a