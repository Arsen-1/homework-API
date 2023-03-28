import requests
import pytest
import json
import jsonpath


def test_get_authors():

    base_url = "https://fakerestapi.azurewebsites.net/"
    endpoint = "api/v1/Authors/"

    response = requests.get(base_url + endpoint)
    assert response.status_code == 200, "status code not match"
    print(response)
    print(response.status_code)
    print(response.json())

def test_get_authors_id():

    base_url = "https://fakerestapi.azurewebsites.net/"
    endpoint = "api/v1/Authors/1"

    response = requests.get(base_url + endpoint)
    assert response.status_code == 200, "status code not match"
    print(response)
    print(response.status_code)

def test_get_book_id():

    base_url = "https://fakerestapi.azurewebsites.net/"
    end_point = "/api/v1/Authors/authors/books/1"

    response = requests.get(base_url + end_point)
    assert response.status_code == 200, "status code not match"
    print(response)
    print(response.status_code)
    print(response.text)
    print(response.headers)

def test_create_authors():
    request_json = {
        'id': 0,
        'idBook': 0,
        'name': 'Arsen',
        'lastName': 'Gevorgyan'}

    base_url = "https://fakerestapi.azurewebsites.net/"
    end_point = "api/v1/Authors/"

    response = requests.post(base_url + end_point, json = request_json)
    assert response.status_code == 200, "status code not match"
    print(response)
    print(response.status_code)

def test_update_authors():
    request_json = {
        "id": 0,
        "title": "string",
        "dueDate": "2023-03-20T18:28:53.398Z",
        "completed": True}

    base_url = "https://fakerestapi.azurewebsites.net/"
    end_point = "api/v1/Activities/1"

    response = requests.put(base_url + end_point, json=request_json)
    assert response.status_code == 200, "status code not match"
    print(response)
    print(response.status_code)

def test_delete_author():

    base_url = "https://fakerestapi.azurewebsites.net/"
    end_point = "/api/v1/Authors/1"

    response = requests.delete(base_url + end_point)
    assert response.status_code == 200, "Status code not match"
    print(response)
    print(response.status_code)