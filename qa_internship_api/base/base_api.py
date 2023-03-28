import json
import requests
import jsonpath as jsn

class BaseApi:
    def get_request(self, url, params=None, headers=None):
        """

        Use this method to send the get answer
        :param url: The request URL
        :param params: The request params (OPTIONAL)
        :param headers: The request headers (OPTIONAL)
        :return: response
        """
        response = requests.get(url, params=params, headers=headers, verify=False)
        return response

    def post_request(self, url, json_date, headers=None):
        """

        :param url:
        :param json_date:
        :param headers:
        :return:
        """
        response = requests.post(url, json_date, headers=headers, verify=False)
        return response



    def put_request(self, url, json_date, headers=None):
        """

        :param url:
        :param json_date:
        :param headers:
        :return:
        """

        response = requests.put(url, json_date, headers=headers, verify=False)
        return response

    def delete_request(self, url, json_date, headers=None):
        """

        :param url:
        :param json_date:
        :param headers:
        :return:
        """

        response = requests.delete(url, json=json_date, headers=headers, verify=False)
        return response




    def check_status_code(self, response, expected_status_code):
        """
        Use this method to check the responce status 
        :param responce:
        :param expected_status_code:
        :return:
        """
        assert response.status_code == expected_status_code

    def check_json_values_by_key(self, response, key):

        json_data = json.loads(response.text)
        values_in_json = jsn.jsonpath(json_data, key)
        return values_in_json
    
    
    def check_json_value(self, values_list, expected_value):
        for val in values_list:
            if val == expected_value:
                return val
        