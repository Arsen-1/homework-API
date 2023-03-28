from qa_internship_api.endpoints.products import Products
import json
def test_get_product(app_config):
    product = Products()

    prod_list = product.get_products(app_config.base_url, 200)
    product.get_products(app_config.base_url + product.get_product_endpoint, 200)
    assert len(prod_list) == 18  # assuming there are 10 products in the database
    for prod in prod_list:
        assert 'id' in prod
        assert 'name' in prod
        assert 'price' in prod

    expected_prod = {'id': 1, 'name': 'Bamboo Thermal Ski Coat', 'price': 99.00}
    prod_list = product.get_products(app_config.base_url, 200, 'Bamboo Thermal Ski Coat')
    assert len(prod_list) == 1
    assert prod_list[0] == expected_prod

    prod_list = product.get_products(app_config.base_url, 400, 'Invalid Product')
    assert prod_list == None

def test_create_product(app_config):
    product = Products()
    new_prod = {'name': 'New Product', 'price': 50}
    product.create_product(app_config.base_url, json.dumps(new_prod))
    prod_list = product.get_products(app_config.base_url, 200)
    assert len(prod_list) == 19

def test_update_product(app_config):
    product = Products()

    #new_prod = {'name': 'New Product', 'price': 50}
    #product.create_product(app_config.base_url, json.dumps(new_prod))

    new_prod_id = product.find_id_by_name(app_config.base_url, 200, 'New Product')
    assert new_prod_id is not None

    updated_prod = {'id': new_prod_id, 'name': 'Updated Product', 'price': 75}
    product.edit_product(app_config.base_url, json.dumps(updated_prod))

    updated_prod_info = product.update_product_endpoint(app_config.base_url, new_prod_id)

    assert updated_prod_info['name'] == 'Updated Product'
    assert updated_prod_info['price'] == 75

def test_delete_product(app_config):
    product = Products()
    new_prod = {'name': 'New Product', 'price': 50}
    product.create_product(app_config.base_url, json.dumps(new_prod))

    prod_list = product.get_products(app_config.base_url, 200)
    last_prod_id = prod_list[-1]['id']

    product.delete_product(app_config.base_url, json.dumps({'id': last_prod_id}))

    prod_list = product.get_products(app_config.base_url, 200)
    assert len(prod_list) == 18
