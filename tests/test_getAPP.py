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
sql="""SELECT `token`, `display_name`, `app_name`, `prueba`, `coderesponse` FROM `get_app` WHERE prueba='getAPP' """
cursor.execute(sql)
getAPP_CP10=[]
for fila in cursor:
 getAPP_CP10.append(fila)

@pytest.mark.parametrize("token,display_name,app_name,prueba,coderesponse",getAPP_CP10)
def test_traer_datos_APP(token,display_name,app_name,prueba,coderesponse):
    #token="c3ac3cb4ff2631ddf05178923363b1f44825efe1"
    # Act
    response = requests.get('https://api.appcenter.ms/v0.1/apps', headers={
        "accept": "application/json",
        "X-API-Token": token
    })
    resp_data = json.loads(response.content)

    # Assert
    # check status code
    assert response.status_code == coderesponse
