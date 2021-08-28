from django.http import JsonResponse
from rest_framework.views import APIView
from . import serializers
from . import models


class CreatePizza(APIView):
    """
    method      - POST
    description - This method will create a pizza based on the post data
    status code - 201: Pizza successfully created
                  400: Pizza details missing
                  405: Post method not used
    """

    def post(self, request):
        success_message = {'Success': 'Pizza has been added'}
        serializer = serializers.PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(success_message, status=201)
        return JsonResponse(serializer.errors, status=400)


class GetPizzaList(APIView):
    """
        method      - GET
        description - This method will return a list of Pizza available
        status code - 200: Successfully generated pizza list
                      405: Post method not used
    """

    def get(self, request):
        pizza_list = models.Pizza.objects.all()
        serializer = serializers.PizzaSerializer(pizza_list, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


def get_pizza(id):
    try:
        return models.Pizza.objects.get(id=id)
    except models.models.ObjectDoesNotExist:
        not_found = {'Error': 'Pizza not found'}
        return JsonResponse(not_found, status=404)


class GetPizza(APIView):
    """
        method      - GET
        description - This method will return the information about the pizza
        status code - 200: Successfully generated pizza details
                      404: Pizza details not found

    """

    def get(self, request, id):
        pizza = get_pizza(id)
        if isinstance(pizza, models.Pizza):
            serializer = serializers.PizzaSerializer(pizza)
            return JsonResponse(serializer.data, status=200)
        return pizza


class EditPizza(APIView):
    """
        method      - PUT
        description - This method will edit a pizza with the information provided
        status code - 200: Pizza edited successfully
                      400: Pizza details missing
                      404: Pizza details not found

    """

    def put(self, request, id):
        success_message = {'Success': 'Updated successfully'}
        pizza = get_pizza(id)
        if isinstance(pizza, models.Pizza):
            serializer = serializers.PizzaSerializer(pizza, request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(success_message, status=200)
            return JsonResponse(serializer.errors, status=400)
        return pizza


class DeletePizza(APIView):
    """
        method      - DELETE
        description - This method will delete a pizza
        status code - 200: Pizza successfully deleted
                      404: Pizza details not found

    """

    def delete(self, request, id):
        success_message = {'Success': 'Deleted successfully'}
        pizza = get_pizza(id)
        if isinstance(pizza, models.Pizza):
            pizza.delete()
            return JsonResponse(success_message, status=200)
        return pizza
