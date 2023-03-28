from qa_internship_api.base.base_api import BaseApi


class Categories(BaseApi):
    get_category_endpoints = "/api_testing/category/read.php"
    def get_categories(self, url, expected_status_code, expected_category):

        response = self.get_request(url)
        self.check_status_code(response, expected_status_code)
        json_list = self.check_json_values_by_key(response, "$.records..name")
        exp_value = self.check_json_value(json_list, expected_category)
        assert exp_value == expected_category, f"exp_value {exp_value} not match with {expected_category}"


