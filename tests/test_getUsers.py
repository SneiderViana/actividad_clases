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
sql="""SELECT `token`, `id`, `display_name`, `email`, `name`, `avatar_url`, `can_change_password`, `created_at`, `origin`, `coderesponse`,`prueba` FROM `get_users` WHERE CODERESPONSE='200' """
cursor.execute(sql)
resultados=[]
for fila in cursor:
 resultados.append(fila)

cursor=connection.cursor()
sql="""SELECT `token`, `id`, `display_name`, `email`, `name`, `avatar_url`, `can_change_password`, `created_at`, `origin`, `coderesponse`,`prueba` FROM `get_users`  WHERE prueba='token_incorrecto' """
cursor.execute(sql)
resultados_tokenIncorrecto=[]
for fila in cursor:
 resultados_tokenIncorrecto.append(fila)


@pytest.mark.parametrize("token, id, display_name, email, name, avatar_url, can_change_password, created_at, origin, coderesponse, prueba", resultados)
def test_traer_datos_usuario(token, id, display_name, email, name, avatar_url, can_change_password, created_at, origin, coderesponse,prueba):
    userdata= {"id": id,
                "display_name": display_name,
                "email": email,
                "name": name,
                "avatar_url": None,
                "can_change_password": False,
                "created_at": created_at ,
                "origin": origin}
    # Act
    response = requests.get('https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json",
        "X-API-Token": token
    })
    resp_data = json.loads(response.content)

    # Assert
    # check status code
    assert response.status_code == coderesponse
    # verify that the json returns the user information
    assert resp_data == userdata

@pytest.mark.parametrize("token, id, display_name, email, name, avatar_url, can_change_password, created_at, origin, coderesponse, prueba", resultados_tokenIncorrecto)
def test_traer_datos_usuario_token_noauth(token, id, display_name, email, name, avatar_url, can_change_password, created_at, origin, coderesponse,prueba):
    userdata= {"message": "Missing valid authentication token. Correlation ID: 11ea43f2-79d4-4fb8-9894-d5f3233dfbf7",
               "statusCode": 401,
               "code": "Unauthorized"}
    # Act
    response = requests.get('https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json"
    })
    resp_data = json.loads(response.content)
    # Assert
    # check status code
    assert response.status_code == 401
    # verify that the json returns the user information
    assert resp_data["code"] == userdata["code"]


def test_traer_datos_usuario_Tokenmal():
    token_ml= "44553a4d814c683dba358422dd900ae70" 
    userdata= {"message": "Unauthorized. Correlation ID: 87933c1f-9fe5-45d8-b338-4fd3edc60d3c",
                "statusCode": 401,
                "code": "Unauthorized"}
    # Act
    response = requests.get('https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json",
        "X-API-Token": token_ml
    })
    resp_data = json.loads(response.content)
    # Assert
    # check status code
    assert response.status_code == 401
    # verify that the json returns the user information
    assert resp_data["code"] == userdata["code"]
