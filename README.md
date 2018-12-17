[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

[![Build Status](https://travis-ci.com/aorzh/shopstyle_api.svg?branch=master)](https://travis-ci.com/aorzh/shopstyle_api)

#API client for Shopstylecollective

## Installing

 `pip install shopstyle_api`

To getting access to shopstylecollective api write in your code:

`from shopstyle_api.api import ShopStyleApi`

or shortly

`from shopstyle_api import ShopStyleApi`

and 

`client = ShopStyleApi(api_key=SHOPSTYLE_API_KEY, api_username=YOUR_USERNAME)`


***If you looking some examples please look at tests forlder.***


-------------

## List of available methods

* `get_brands()` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000844306--brands)

* `get_categories()` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000868763--categories)

* `get_colors()` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000864683--colors)

* `get_lists()` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000845806--lists)

* `get_list_id(list_id)` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866203--lists-list-id-)

* `get_list_items(list_id, limit, offset`) (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000845926--lists-list-id-items)

* `get_price_filters()` (https://shopstylecollective.zendesk.com/hc/en-us/articles/360001337531--Price-Filters)

* `get_product(product_id, free_text_search, category, filters, pdd, sort)` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866043-What-are-the-query-parameters-)

* `get_products(filters, category, floor, free_text_search, pdd, sort,
                     limit, offset)` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866043-What-are-the-query-parameters-)

* `get_products_histogram(filters, category, floor, free_text_search, pdd, sort)` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000866043-What-are-the-query-parameters-)

* `get_retailers()` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000868743--retailers)

**DEPRECATED BELOW**
*rerun only {"errorCode":400,"errorMessage":"HTTP 404 Not Found"}*
* `list_search(list_id, free_text_search, filters, category, sort, limit, offset)` (https://shopstylecollective.zendesk.com/hc/en-us/articles/115000848706--lists-search)





