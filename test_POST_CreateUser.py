import allure
import requests

from MYAPI.Utilities.Payload import post_payload
from MYAPI.Utilities.configuration import getconfig

@allure.severity(allure.severity_level.NORMAL)
def test_adduser():
    URL=getconfig()['API']['endpoint'] +'add'
    response=requests.post(URL,post_payload())
    print(response.json())
    assert response.status_code==201

@allure.severity(allure.severity_level.NORMAL)
def test_404error():
    URL=getconfig()['API']['endpoint']
    response =requests.post(URL,post_payload())
    assert response.status_code==404

