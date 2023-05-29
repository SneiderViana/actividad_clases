import pytest
import requests
import json
import mysql.connector

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="",
        database='dbtesttdd'
    )
    if connection.is_connected():
        print("conexion exitosa")
        info_server=connection.get_server_info()
        print(info_server)
except Exception as ex:
    print(ex)

cursor=connection.cursor()
sql="""SELECT `token`, `owner_name`, `app_name`, `prueba`, `coderesponse` FROM `delete_app` WHERE PRUEBA ='deleteAPP'"""
cursor.execute(sql)
delete_APP_list=[]
for fila in cursor:
 delete_APP_list.append(fila)

@pytest.mark.parametrize("token,owner_name,app_name, prueba, coderesponse", delete_APP_list)
def test_delete_APP(token,owner_name,app_name, prueba, coderesponse):
    #token= "44553a4d814c683dba358422dd900ae70f0a3d97" 
    #owner_name="sdviana-unicesar.edu.co"
    #app_name="prueba3"
    # Act
    response = requests.get(f'https://api.appcenter.ms/v0.1/apps/{owner_name}/{app_name}', headers={
        "accept": "application/json",
        "X-API-Token": token
    })
    resp_data = json.loads(response.content)

    # Assert
    # comprobar codigo de respuesta
    assert response.status_code == coderesponse

cursor=connection.cursor()
sql=""" SELECT `token`, `owner_name`, `app_name`, `prueba`, `coderesponse` FROM `delete_app` WHERE coderesponse='404'"""
cursor.execute(sql)
delete_APPnocreada_list=[]
for fila in cursor:
 delete_APPnocreada_list.append(fila)
@pytest.mark.parametrize("token,owner_name,app_name, prueba, coderesponse", delete_APPnocreada_list)
def test_delete_APP_NOT_CREATE(token,owner_name,app_name, prueba, coderesponse):
   
    # Accion
    response = requests.get(f'https://api.appcenter.ms/v0.1/apps/{owner_name}/{app_name}', headers={
        "accept": "application/json",
        "X-API-Token": token
    })
    resp_data = json.loads(response.content)

    # Assert
    # comprobar codigo de respuesta
    assert response.status_code == coderesponse
   

@pytest.mark.parametrize("token,owner_name,app_name, prueba, coderesponse", delete_APPnocreada_list)
def test_delete_APP_NAME_INCORRECT(token,owner_name,app_name, prueba, coderesponse):

    userdata={"message": "Not found. Correlation ID: 7c12d21d-560e-4a90-a49e-34a88adeb8d5",
               "statusCode": 404,
               "code": "Not Found"}
    # Accion
    response = requests.get(f'https://api.appcenter.ms/v0.1/apps/{owner_name}/{app_name}', headers={
        "accept": "application/json",
        "X-API-Token": token
    })
    resp_data = json.loads(response.content)

     # Assert
     # comprobar codigo de respuesta
    assert response.status_code == coderesponse
     # verify that the json returns the user information
    assert resp_data["code"] == userdata["code"]