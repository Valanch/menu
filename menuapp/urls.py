from django.urls import path
from menuapp import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.index)
]
