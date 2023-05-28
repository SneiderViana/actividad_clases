import pytest
import requests

def test_get_profile_date_of_user():
    token='token' 
    userdata='user'
    # Act
    response = requests.get('https://api.appcenter.ms/v0.1/user', headers={
        "accept": "application/json",
        "X-API-Token": token
    })
    resp_data = json.loads(response.content)

    # Assert
    # check status code
    assert response.status_code == 200
    # verify that the json returns the user information
    assert resp_data == userdata