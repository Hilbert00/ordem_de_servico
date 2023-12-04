"""
URL configuration for mecanica project.

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
from django.contrib import admin
from django.urls import path, include
from mecanica import views

urlpatterns = [
    path("", views.home),
    path("workers/", views.listWorkers),
    path("workers/add/", views.addWorker),
    path("vehicles/", views.listVehicles),
    path("vehicles/add/", views.addVehicle),
    path("clients/", views.listClients),
    path("clients/add/", views.addClient),
    path("services/", views.listServices),
    path("services/add/", views.addService),
    path("orders/", views.listOrders),
    path("orders/add/", views.addOrder),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
