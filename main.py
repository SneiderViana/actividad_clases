from typing import Union
from fastapi import FastAPI

app = FastAPI()


def hola():
    return {"HELLO FASTAPI"}


def Primo(numero): 
     for n in range(2,numero):
       if numero % n == 0:
          return False  
     return True

def fibonnacci(num: int):
     a=0
     b=1
     for n in range(0, num):
        c=a+b
        a=b
        b=c
     return a