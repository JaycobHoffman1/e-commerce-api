# Mini-Project: E-commerce API

- Author: Jaycob Hoffman

- Date: 22 August 2024

## Documentation

"Mini-Project: E-commerce API" uses Python with Flask and SQLAlchemy to simulate users' abilities to create and manage customers and their accounts, add and manage products, as well as place and track orders on an e-commerce web application. This API is designed to be integrated with an e-commerce web application, emulating basic functionalities while prioritizing efficiency and data integrity.

### User Interaction and Main Features

Users can interact with the API by sending requests via Postman. Requests have already been defined and are organized based on the API's main features:

- **Customer Management**: Users can easily add and update customers by entering the name, email address, and phone number of the customer they wish to add in JSON format on Postman. Users can also view and delete customers by entering the customers' unique numeric id's, which are auto-generated by the API. 
- **Customer Account Management**: Users can also create and manage customer accounts by entering the numeric id of the customer they wish to create an account for, as well as a username and password, in JSON format on Postman. Additionally, users can view and delete customer accounts by entering the accounts' unique numeric id's (auto-generated).
- **Product Management**:  Users can create and manage products by entering a product name and price in JSON format on Postman. Users can then view and delete individual products by entering the products' unique numeric id's (auto-generated). Additionally, users can view a list of all products currently available. This list updates in real time with product additions and removals.
- **Order Management**: Finally, users can place orders and view order details. When placing an order, users can enter the id of the customer placing the order, the id of the product they wish to order, as well as the order date and expected delivery date. Users can then enter order's numeric id (auto-generated) view order details, and can "track" the order by noting its expected arrival date.

### Examples of program's functionalities when used with Postman:

- Adding a new customer "John Doe":

```
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "123-456-7890"
}
```

- Creating account for "John Doe" (id of "1"):

```
{
    "username": "JohnDoe",
    "password": "johndoe123",
    "customer_id": 1
}
```

- Listing all available products:

```
[
    {
        "id": 1,
        "name": "T-shirt",
        "price": 19.99
    },
    {
        "id": 2,
        "name": "Denim shorts",
        "price": 24.99
    },
    {
        "id": 3,
        "name": "Baseball cap",
        "price": 11.99
    }
]
```

- Retrieving order details for "Baseball cap" (in transit, id of "3")

```
{
    "customer_id": 1,
    "delivery_date": "2024-08-25",
    "id": 1,
    "order_date": "2024-08-22",
    "product_id": 3
}
```

### Errors

The E-commerce API will raise errors with accompanying messages under the following circumstances:

- ```ValidationError```: If the program is unable to deserialize data for any object ("Customer", "CustomerAccount", "Product", or "Order")
- ```404```: If, when viewing or deleting an object, a user searches for an object by an numeric id that does not exist in the system.

#

View the E-commerce API [GitHub Repository](https://github.com/JaycobHoffman1/e-commerce-api)
