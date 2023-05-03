
def test_Isprime():
    numero=cal.Primo(4)
    assert numero == False

def test_fibinnacci():    
  num=3
  numero=cal.fibonnacci(num)
  assert numero == 2

def test_hola():
    saludo=cal.hello()
    assert  saludo== "HELLO FASTAPI"