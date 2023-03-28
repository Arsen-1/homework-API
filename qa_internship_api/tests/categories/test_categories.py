from qa_internship_api.endpoints.categories import Categories

def test_get_category(app_config):
    category = Categories()
    category.get_categories(app_config.base_url+category.get_category_endpoints, 200, "Supplements")
