from flaskr import company
import json

test_xml ="""<?xml version="1.0" encoding="UTF-8"?><Data><id>1</id><name>MWNZ</name><description>..is awesome</description></Data>"""
test_json_string = {"id": "1", "name": "MWNZ", "description": "..is awesome"}
test_json = json.dumps(test_json_string)

def test_xml_to_json():
    response = company.convert_company_xml_to_json(test_xml)
    assert response == test_json
    
def test_hello_world(client):
    response = client.get('/xml-api/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_get_company_1(client):
    response = client.get('/xml-api/1')
    
    assert response.status_code == 200
    assert response.data is not None

def test_get_company_2(client):
    response = client.get('/xml-api/2')
    
    assert response.status_code == 200
    assert response.data is not None

def test_get_unknown_company(client):
    response = client.get('/xml-api/3')
    
    assert response.status_code == 404

def test_get_invalid_input_symbol(client):
    response = client.get('/xml-api/@@')

    assert response.status_code == 404

def test_get_invalid_input_letters(client):
    response = client.get('/xml-api/aaaa')

    assert response.status_code == 404