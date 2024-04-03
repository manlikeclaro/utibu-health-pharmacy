# API Documentation

## Authentication
- The API uses basic authentication for user authentication.
- For certain endpoints, cookie-based authentication is also required.

## Endpoints

### Pharmacy API
- ` [GET] /pharmacy/api/` : Retrieve pharmacy API information.
- ` [GET] /pharmacy/api/customers/` : List all customers.
  - ` [POST] /pharmacy/api/customers/` : Create new customer.
- ` [GET/PUT/PATCH/DELETE] /pharmacy/api/customers/{id}/` : Retrieve/update/delete customer by ID.
- ` [GET] /pharmacy/api/medications/` : List all medications.
  - ` [POST] /pharmacy/api/medications/` : Create new medication.
- ` [GET/PUT/PATCH/DELETE] /pharmacy/api/medications/{id}/` : Retrieve/update/delete medication by ID.
- ` [GET] /pharmacy/api/orders/` : List all orders.
  - ` [POST] /pharmacy/api/orders/` : Create new order.
- ` [GET/PUT/PATCH/DELETE] /pharmacy/api/orders/{id}/` : Retrieve/update/delete order by ID.

## Request and Response Formats
- Detailed request and response formats are provided for each endpoint.
- See individual endpoint documentation for more information.


## Access Documentation
- To access the detailed API documentation, visit [API Documentation](http://127.0.0.1:8000/pharmacy/api/docs/).
