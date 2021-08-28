from django.db import models


class Pizza(models.Model):
    """
    id       - The integer Identifier of the pizza
    name     - The Name of the pizza
    type     - The Type of pizza: Regular, Square
    size     - The Size of pizza: Small, Medium, Large
    toppings - The Toppings of pizza:
    """

    PIZZA_TYPE = (
        ('R', 'Regular'),
        ('S', 'Square')
    )

    PIZZA_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=PIZZA_TYPE)
    size = models.CharField(max_length=10, choices=PIZZA_SIZE)
    toppings = models.TextField()

    def __int__(self):
        return self.id
