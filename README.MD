# Technical Exam Web_Programming

## Overview

This project contain the Tech-Exam 1 & 2

## Project Information
- Application Structure: The Flask application is structured with models, routes, and services.
- Database: The application uses SQLite for data storage.
- Postman JSON: Also added postman json file for api testing, just import the Trading Application.postman_collection.json to Postman

# API Documentation
This section outlines the various API endpoints available in the Flask Time Tracker application, detailing their purpose and usage.

## Authorization
All API requests require an API key for authentication. The API key should be included in the Authorization header of each request.

```bash
Authorization: Bearer YOUR_API_KEY
```

## Signup

~~### `POST /signup`

* **Description**: Signup a new user to the application.
* **Request Body**:

  | Parameter | Type | Description |
  | :--- | :--- | :--- |
  | `username` | `string` | **Required**. User's desired username. |
  | `email` | `string` | **Required**. User's email address. |
  | `password` | `string` | **Required**. User's chosen password. |
  
  ```json
  {
    "username" : "user",
    "email" : "user@gmail.com",
    "password" : "12345678"
  }
  ```

* **Response**: Returns a success message upon successful signup or an error message on failure.

## Login

### `POST /login`

* **Description**: Authenticate a user and return an access token.
* **Request Body**:

  | Parameter | Type | Description |
    | :--- | :--- | :--- |
  | `username` | `string` | **Required**. User's username. |
  | `password` | `string` | **Required**. User's password. |
  ```json
  {
    "username" : "user",
    "password" : "12345678"
  }~~


Stocks API
-------------

### `GET /stock/stocks`

*   **Description**: Retrieve the all the available stocks
*   **Response**: Returns a list of all stocks, including their IDs, names, and prices



## Order API

### `POST /order/order`

* **Description**: Create a new order for user and stocks.
* **Request Body**:

  | Parameter | Type | Description |
  | :--- | :--- | :--- |
  | `stock_id` | `int` | **Required**. The ID of the stock to order. |
  | `quantity` | `int` | **Required**. The number of stocks to order. |
  | `price` | `float` | **Required**. The price at which the stock is ordered. |

  ```json
  {
    "stock_id": 1,
    "quantity": 10,
    "price": 150.50
  }

Portfolio API
-------------

### `GET /order/portfolio/<stock_id>`

*   **Description**: Retrieve the total value invested in the user’s portfolio on all and specific stocks.

* **URL Parameters**:

  | Parameter | Type | Description                        |
    | :--- |:-----------------------------------| :--- |
  | `stock_id` | `int` | **Optional**. The ID of the stock. |

