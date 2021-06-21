import requests

from MYAPI.Utilities.configuration import getconfig
def test_deleteuser():
    url=getconfig()['API']['endpoint'] +"delete/2"
    response=requests.delete(url)
    print(response.json())
    assert response.status_code==200
def test_errorhandle():
    url= getconfig()['API']['endpoint']
    response=requests.delete(url)
    print(response.json())
    assert response.status_code==404