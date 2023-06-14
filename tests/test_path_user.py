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
sql="""SELECT `token`, `display_name`, `coderesponse`, `prueba` FROM `patch_user` WHERE prueba='ModificaCP7'"""
cursor.execute(sql)
ModificaCP7_user_list=[]
for fila in cursor:
 ModificaCP7_user_list.append(fila)

@pytest.mark.parametrize("token,display_name,coderesponse,prueba",ModificaCP7_user_list)
def test_usuario_modificado(token,display_name,coderesponse,prueba):
    #token= "44553a4d814c683dba358422dd900ae70f0a3d97" 
    #display_name_Actualizado ="valentina rodriguez"  
    # Accion
    response = requests.patch(f'https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-API-Token": token
    },json={
        "display_name": display_name
    })
    resp_data = json.loads(response.content)

    # Assert
    # comprobar codigo de respuesta
    assert response.status_code == coderesponse
    #comprobar cuerpo de respuesta
    assert resp_data["display_name"]==display_name

cursor=connection.cursor()
sql="""SELECT `token`, `display_name`, `coderesponse`, `prueba` FROM `patch_user` WHERE prueba='ModificaCP8'"""
cursor.execute(sql)
ModificaCP8_user_list=[]
for fila in cursor:
  ModificaCP8_user_list.append(fila)

@pytest.mark.parametrize("token,display_name,coderesponse,prueba",ModificaCP8_user_list)
def test_usuario_modificado_CP8(token,display_name,coderesponse,prueba):
    #token= "44553a4d814c683dba358422dd900ae70f0a3d97" 
    #display_name_Actualizado ="valentina rodriguez"  
    # Accion
    response = requests.patch(f'https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json",
        "Content-Type": "application/json"
    },json={
        "display_name": display_name
    })
    resp_data = json.loads(response.content)

    # Assert
    # comprobar codigo de respuesta
    assert response.status_code == coderesponse

@pytest.mark.parametrize("token,display_name,coderesponse,prueba",ModificaCP7_user_list)
def test_usuario_modificado_CP9(token,display_name,coderesponse,prueba):
    #token= "44553a4d814c683dba358422dd900ae70f0a3d97" 
    #display_name_Actualizado ="valentina rodriguez"  
    # Accion
    response = requests.patch(f'https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-API-Token": token
    },json={
    })
    resp_data = json.loads(response.content)

    # Assert
    # comprobar codigo de respuesta
    assert response.status_code == 400
   

