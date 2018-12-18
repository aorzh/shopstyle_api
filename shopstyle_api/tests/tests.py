import os
import unittest
from shopstyle_api.api import ShopStyleApi


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api_key = os.environ['SHOPSTYLE_API_KEY']
        self.api_username = os.environ['SHOPSTYLE_API_USERNAME']
        self.client = ShopStyleApi(api_key=self.api_key, api_username=self.api_username)
        self.list_id = 48317762
        self.product_id = 754386152
        self.category = 'women'
        self.fts = ''  # filters
        self.brand_id = 2333  # Forever 21

    def test_wrong_credentials(self):
        client = ShopStyleApi(api_key='', api_username='')
        result = client.get_brands()

        self.assertEqual(result.get('errorCode'), 401)
        self.assertEqual(result.get('errorName'), 'MissingPartnerId')

    def test_get_brands(self):
        result = self.client.get_brands()
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('brands'), list))

    def test_get_categories(self):
        result = self.client.get_categories()
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('categories'), list))

    def test_get_colors(self):
        result = self.client.get_colors()
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('colors'), list))

    def test_get_lists(self):
        result = self.client.get_lists()
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('lists'), list))

    def test_get_list_id_wrong_id(self):
        list_id = 0
        result = self.client.get_list_id(list_id)
        self.assertEqual(result.get('errorCode'), 404)
        self.assertEqual(result.get('errorName'), 'FavoriteListNotFound')

    def test_get_list_id(self):
        result = self.client.get_list_id(self.list_id)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result.get('id'), self.list_id)
        self.assertTrue(isinstance(result.get('favorites'), list))

    def test_get_list_items_no_limit(self):
        result = self.client.get_list_items(self.list_id)
        self.assertEqual(result.get('metadata').get('limit'), 50)
        self.assertTrue(isinstance(result.get('favorites'), list))

    def test_get_list_items(self):
        result = self.client.get_list_items(self.list_id, limit=1)
        self.assertEqual(result.get('metadata').get('limit'), 1)
        self.assertTrue(isinstance(result.get('favorites'), list))

    def test_get_price_filters(self):
        result = self.client.get_price_filters()
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('priceFilters'), list))

    def test_get_product_wrong_id(self):
        product_id = 0
        result = self.client.get_product(product_id)
        self.assertEqual(result.get('errorCode'), 404)
        self.assertEqual(result.get('errorName'), 'InvalidProductId')

    def test_get_product_by_id(self):
        result = self.client.get_product(self.product_id)
        self.assertEqual(result.get('id'), self.product_id)

    def test_get_product_by_filters(self):
        """
        Filter by brand 'Forever 21'
        :return:
        """
        filters = [f'b{self.brand_id}', ]
        result = self.client.get_products(filters=filters)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('products'), list))

    def test_get_products_histogram(self):
        filters = [f'b{self.brand_id}']
        result = self.client.get_products(filters=filters)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('products'), list))

    def test_get_retailers(self):
        result = self.client.get_retailers()
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result.get('retailers'), list))

    def test_get_list_search_not_found(self):
        filters = ['b{123123123123123123}']
        result = self.client.list_search(self.list_id, filters=filters)
        self.assertEqual(result.get('errorCode'), 400)

    def test_get_list_search(self):
        filters = [f'b{self.brand_id}']
        result = self.client.list_search(self.list_id, filters=filters)
        self.assertEqual(result.get('errorCode'), 400)


if __name__ == '__main__':
    unittest.main()
