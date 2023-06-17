"""
URL configuration for GrocerE_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.grocery_list, name='grocery_list'),
    path('detail/<int:item_id>/', views.grocery_detail, name='grocery_detail'),
    path('edit/<int:item_id>/', views.grocery_edit, name='grocery_edit'),
    path('cart.json', views.cart_json, name='cart_json'),
]
