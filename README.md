# omnisdk

# Documentation

Note:
There won't be a separate documentation up until the very first stable release. The public api may change heavily until
release 1.0.0

### Installation

Currently, this library has no published version. You can - however - install and use the library from the master branch
using git and pip

```bash
python -m pip install omnisdk
```

### Quick Start

```python

from omnisdk.omnitron.client import OmnitronApiClient
from omnisdk.omnitron.endpoints import ProductEndpoint
from omnisdk.omnitron.models import Product

api = OmnitronApiClient(base_url="base_url", username="username", password="password")
# Create
# products/
endpoint = ProductEndpoint() #You can check the path of the endpoint classes
product = Product(sku="123")
product.name = "My product"

#POST /products/
new_product = endpoint.create(item=product) # This returns a Product instance

# Update
#PATCH /products/<pk>/
updated_product = endpoint.update(id=new_product.pk, item=new_product)

# Delete
#DELETE /products/<pk>/
endpoint.delete(id=new_product.pk)

# List
#GET /products/<pk>/?attributes__color=blue
products = endpoint.list(params={"attributes__color": "blue"}) #First page of all products

# Pagination
#GET /products/?attributes__color=blue
#GET /products/?attributes__color=blue&page=2
#GET /products/?attributes__color=blue&page=3
#...

for product_batch in endpoint.iterator:
    products.extend(product_batch)

# Get only next page, might raise StopIteration, 
# note that another call to .list will continue give its next pages    
next_page_of_products = next(endpoint.iterator)

# Filter
blue_products = endpoint.list(params={"attributes__color": "blue"})
    
# Nested rest queries
from omnisdk.omnitron.endpoints import ChannelProductEndpoint
# channel/{channel_id}/products/
endpoint = ChannelProductEndpoint(channel_id=1, path="inserts")

# GET /channel/1/products/inserts/
endpoint.list()
# There is no update service on this path however we are putting this here to demonstrate 
# how omnisdk can be called
# PATCH /channel/1/products/22/inserts/
endpoint.update(id=product.pk, item=product)

del api  # This closes the session
# normally garbage collected in CPython, but you can do it manually

## Alternatively

with OmnitronApiClient(base_url="base_url", username="username", password="password"):
    endpoint = ProductEndpoint()
    product = Product(sku="123")
    product.name = "My product"
    endpoint.create(item=product)
    
# The session is closed by the context manager

```

## Detailed Information About omnisdk Behaviour

* Endpoint classes searches whether there is a client instance initialized and uses that client.
  Notice that we do not use the `as` keyword in the `with` block. Endpoint classes know the client
  class name beforehand and use one of the active instances.

* Endpoint methods take request body with `item` parameter and return the response. Both the requests
  and responses are instances of `model` classes defined in the endpoint classes. If you prefer to
  use JSON as request and response, pass `raw=True` to any endpoint class initialization. List responses
  will return list of dict
  ```python
  endpoint = ProductEndpoint(raw=True)
  endpoint.list() # -> List[dict]
  new_product = endpoint.create(item=product) # item: dict
  # new_product: dict  
  ```
  
* `raw` parameter can only be supplied to endpoint at initialization(\__init\__) not 
  at endpoint calls(\__call\__).

* Endpoint remembers the last `path` parameter supplied. If you do not nullify it, further calls
  will use the last `path` parameter which might be unwanted.

* If you inherit BaseClient class, you can use the same client structure for your own APIs 
  however feature requests related these will not be accepted.



## Design choices needed.

- Do we want to have a dynamic api wrapper that reads the api and creates endpoints, or do we want some static info and
  have sane intellisense support when we use the library?
- We can test by either mocked responses or with an actual live test api. (We can simply get one up in the pipeline with
  all release pushes, shouldn't take much of a resource on bitbucket side)
- We can CRUDL endpoint class instances inside ApiEndpoint, `api.endpoints.crud_action` could be a
  `CrudAction # Delete, Retrieve, etc...` class instance with some common attributes like meta, options, and other kinds
  of relevant methods, like `page` method for `List(CrudAction)` class. The public api would stay the same given that we
  add the relevant `__call__` methods to `CrudAction`, but would have *extra* information about the endpoints, and
  would allow easier manipulation directly from the sdk without needing too much business logic in the end users' code.

## Development

- For development please install `pre-commit` and use >python3.8.
- Tests are handled by `tox`, to run tests simply install it and run `tox` command

## Testing

The tests of this library depends on the actual api, current setup for tests requires you to have three environment
variables available at the time of running the tests. Without these environment variables tests will refuse to run.

- OMNITRON_URL: omnitron base url to test against
- OMNITRON_USERNAME: a valid username for the api
- OMNITRON_PASSWORD: a valid password for the api for the OMNITRON_USERNAME

## Support

It may work on all Python 3 versions however only Python 3.8+ will be tested and supported.