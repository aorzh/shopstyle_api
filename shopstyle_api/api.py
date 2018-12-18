import requests
from .exceptions import ApiKeyNotFound


class ShopStyleApi(object):
    """
    Brand API
    Category API
    Color API
    Retailer API
    Product API
    List API
    Report API
    """
    api_key = ''
    api_username = ''
    api_version = 'v2'
    base_url = 'http://api.shopstyle.com/api/{}'.format(api_version)

    def __init__(self, api_key, api_username, *args, **kwargs):
        self.api_key = api_key
        self.api_username = api_username
        super().__init__()

    @staticmethod
    def build_filters_string(filters_list):
        return '&'.join([f'fl={f}' for f in filters_list])

    def get_lists(self):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000845806--lists
        :return:
        """
        url = f'{self.base_url}/lists/?pid={self.api_key}&userId={self.api_username}'
        r = requests.get(url=url)
        return r.json()

    def get_list_id(self, list_id):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866203--lists-list-id-
        :param list_id:
        :return:
        """
        url = f'{self.base_url}/lists/{list_id}/?pid={self.api_key}'
        r = requests.get(url=url)
        return r.json()

    def get_list_items(self, list_id, limit=50, offset=0):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000845926--lists-list-id-items
        :param list_id:
        :param limit:
        :param offset:
        :return:
        """
        url = f'{self.base_url}/lists/{list_id}/items/?pid={self.api_key}&limit={limit}&offset={offset}'

        r = requests.get(url=url)
        return r.json()

    def list_search(self, list_id='', free_text_search='', filters=None, category='',
                    sort='Recency', limit=50, offset=0):
        """
        LOOKS LIKE THIS ENDPOINT IS DEPRECATED. RETURNING ONLY **{"errorCode":400,"errorMessage":"HTTP 404 Not Found"}**
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000848706--lists-search
        :param list_id:
        :param free_text_search:
        :param filters: list of filters. Filter prefixes are:
                b - brand
                r - retailer
                p - price
                d - sale
                s - size
                c - color
                format <prefix><id> (ex. b1234)
        :param category:
        :param sort:
        :param limit:
        :param offset:
        :return:
        """
        if filters:
            filters = self.build_filters_string(filters)
        url = f'{self.base_url}/lists/search?pid={self.api_key}' \
              f'&userId={self.api_username}&listId={list_id}' \
              f'&fts={free_text_search}&cat={category}&sort={sort}&limit={limit}&offset={offset}&fl={filters}'

        r = requests.get(url=url)
        return r.json()

    def get_brands(self):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000844306--brands
        :return:
        """
        url = f'{self.base_url}/brands/?pid={self.api_key}&userId={self.api_username}'

        r = requests.get(url=url)
        return r.json()

    def get_colors(self):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000864683--colors
        :return:
        """
        url = f'{self.base_url}/colors/?pid={self.api_key}&userId={self.api_username}'

        r = requests.get(url=url)
        return r.json()

    def get_categories(self):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000868763--categories
        :return:
        """
        url = f'{self.base_url}/categories/?pid={self.api_key}&userId={self.api_username}'

        r = requests.get(url=url)
        return r.json()

    def get_retailers(self):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000868743--retailers
        :return:
        """
        url = f'{self.base_url}/retailers/?pid={self.api_key}&userId={self.api_username}'

        r = requests.get(url=url)
        return r.json()

    def get_price_filters(self):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/360001337531--Price-Filters
        :return:
        """
        url = f'{self.base_url}/priceFilters/?pid={self.api_key}&userId={self.api_username}'

        r = requests.get(url=url)
        return r.json()

    def get_product(self, product_id):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866043-What-are-the-query-parameters-
        :param product_id:
        """
        url = f'{self.base_url}/products/{product_id}/?pid={self.api_key}&userId={self.api_username}'
        r = requests.get(url=url)
        return r.json()

    def get_products_histogram(self, filters, category='', floor=0, free_text_search='', pdd='', sort='Recency'):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866043-What-are-the-query-parameters-
        :param filters: list of filters. Available Brand, Retailer, Price, Discount, Size and Color.
        :param category:
        :param floor:
        :param free_text_search:
        :param pdd: A "price drop date" expressed as a number of milliseconds since Jan 1, 1970.
         If present, limits the results to products whose price has dropped since the given date.
        :return:
        :param sort: Available PriceLoHi, PriceHiLo, Recency, Popular
        :return:
        """
        filters = self.build_filters_string(filters)
        url = f'{self.base_url}/products/histogram/?pid={self.api_key}' \
              f'&userId={self.api_username}&floor={floor}&fts={free_text_search}' \
              f'&cat={category}&filters={filters}&pdd={pdd}&sort={sort}'

        r = requests.get(url=url)
        return r.json()

    def get_products(self, filters, category='', floor=0, free_text_search='', pdd='', sort='Recency',
                     limit=50, offset=0):
        """
        https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866043-What-are-the-query-parameters-
        :param filters: list of filters. Available Brand, Retailer, Price, Discount, Size and Color.
        :param category:
        :param floor:
        :param free_text_search:
        :param pdd: A "price drop date" expressed as a number of milliseconds since Jan 1, 1970.
         If present, limits the results to products whose price has dropped since the given date.
        :return:
        :param sort: Available PriceLoHi, PriceHiLo, Recency, Popular
        :param limit:
        :param offset:
        :return:
        """
        filters = self.build_filters_string(filters)
        url = f'{self.base_url}/products/?pid={self.api_key}' \
              f'&userId={self.api_username}&floor={floor}&fts={free_text_search}' \
              f'&cat={category}&filters={filters}&pdd={pdd}&sort={sort}&limit={limit}&offset={offset}'

        r = requests.get(url=url)
        return r.json()

