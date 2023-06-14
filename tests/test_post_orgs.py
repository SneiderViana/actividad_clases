import pytest
import requests
import json
import mysql.connector

try:
    connection=mysql.connector.connect(
       host='database',
        port=3306,
        user='admin',
        password="admin",
        database='dbtesttdd'
    )
    if connection.is_connected():
        print("conexion exitosa")
        info_server=connection.get_server_info()
        print(info_server)
except Exception as ex:
    print(ex)

cursor=connection.cursor()
sql="""SELECT `token`, `display_name`, `name`, `prueba`, `coderesponse` FROM `post_orgs` WHERE prueba='pruebaCP13'"""
cursor.execute(sql)
postORGS_CP13=[]
for fila in cursor:
 postORGS_CP13.append(fila)

@pytest.mark.parametrize("token, display_name, name, prueba, coderesponse",postORGS_CP13)
def test_post_orgs(token, display_name, name, prueba, coderesponse):
    #token="c3ac3cb4ff2631ddf05178923363b1f44825efe1"
    # Act
    response = requests.post(f'https://api.appcenter.ms/v0.1/orgs', headers={
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-API-Token": token
    },json={
        "display_name": display_name,
        "name": name
    })
    resp_data = json.loads(response.content)

    # Assert
    # check status code
    assert response.status_code == coderesponse

@pytest.mark.parametrize("token, display_name, name, prueba, coderesponse",postORGS_CP13)
def test_post_orgs_tokens(token, display_name, name, prueba, coderesponse):
    #token="c3ac3cb4ff2631ddf05178923363b1f44825efe1"
    # Act
    response = requests.post(f'https://api.appcenter.ms/v0.1/orgs', headers={
        "accept": "application/json",
        "Content-Type": "application/json"
       
    },json={
        "display_name": display_name,
        "name": name
    })
    resp_data = json.loads(response.content)

    # Assert
    # check status code
    assert response.status_code == 401

@pytest.mark.parametrize("token, display_name, name, prueba, coderesponse",postORGS_CP13)
def test_post_orgs_error(token, display_name, name, prueba, coderesponse):
    #token="c3ac3cb4ff2631ddf05178923363b1f44825efe1"
    # Act
    response = requests.post(f'https://api.appcenter.ms/v0.1/orgs', headers={
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-API-Token": token
    },json={
        "display_name": display_name,
        "nombre": name
    })
    resp_data = json.loads(response.content)

    # Assert
    # check status code
    assert response.status_code == 400