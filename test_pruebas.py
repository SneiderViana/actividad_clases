from main import * 

def test_Isprime():
    numero=Primo(4)
    assert numero == False

def test_fibinnacci():    
  num=3
  numero=fibonnacci(num)
  assert numero == 2

def test_hola():
    saludo=hello()
    assert  saludo == "HELLO FASTAPI"