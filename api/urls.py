from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreatePizza.as_view(), name='create'),
    path('list', views.GetPizzaList.as_view(), name='list'),
    path('get/<int:id>', views.GetPizza.as_view(), name='get'),
    path('edit/<int:id>', views.EditPizza.as_view(), name='edit'),
    path('delete/<int:id>', views.DeletePizza.as_view(), name='delete')
]
