import allure
import requests
from MYAPI.Utilities.configuration import getconfig



@allure.severity(allure.severity_level.NORMAL)
def test_Userlist():
    url=getconfig()['API']['endpoint'] + 'users'
    response=requests.get(url,)
    list_data=response.json()
    print(list_data)
    assert response.status_code==200
    for obj in list_data:
        if obj[0]=='Priyanka Mohaldar':
            print(obj[0])
            break
@allure.severity(allure.severity_level.MINOR)
def test_User():
    url=getconfig()['API']['endpoint'] + 'user/5'
    respose=requests.get(url,)
    data=respose.json()
    print(data)
    assert respose.status_code==200

@allure.severity(allure.severity_level.CRITICAL)
def test_error():
    url =getconfig()['API']['endpoint']
    response=requests.get(url,)
    print(response.json())
    assert response.status_code==404