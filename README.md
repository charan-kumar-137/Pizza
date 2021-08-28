# Pizza

### Overview
A application to store information about different types of pizza.
Pizza can be of multiple types and sizes and can have toppings.
An API to retrieve, create, modify and delete the pizza

### Technology
* **[Django](https://www.djangoproject.com/)**
* **[MongoDB](https://www.mongodb.com/)**

### API
The API endpoints are:

| Endpoind       | Description         |Method |
|----------------|---------------------|:-----:|
|create          |Create a Pizza       |POST   |
|list            |Get list of Pizzas   |GET    |
|get/pizza_id    |Get details of Pizza |GET    |
|edit/pizza_id   |Edit the Pizza       |PUT    |
|delete/pizza_id |Delete the Pizza     |DELETE |

### Installation
Clone the repository

`git clone https://github.com/charan-kumar-137/Pizza`

Create a virtual environment and activate it

Go to project root directory

`cd Pizza`

Install the requirements

`pip install -r requirements.txt`

Migrate the model to database scheme

`python manage.py migrate`

Start the server 

`python manage.py runserver`

### Usage
The api can be accessed at http://127.0.0.1:8000/api/
