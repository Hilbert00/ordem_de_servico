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
    path("workers/edit/<int:id>/", views.editWorker),
    path("workers/delete/<int:id>/", views.deleteWorker),
    path("vehicles/", views.listVehicles),
    path("vehicles/add/", views.addVehicle),
    path("vehicles/edit/<int:id>/", views.editVehicle),
    path("vehicles/delete/<int:id>/", views.deleteVehicle),
    path("clients/", views.listClients),
    path("clients/add/", views.addClient),
    path("clients/edit/<int:id>/", views.editClient),
    path("clients/delete/<int:id>/", views.deleteClient),
    path("services/", views.listServices),
    path("services/add/", views.addService),
    path("services/edit/<int:id>/", views.editService),
    path("services/delete/<int:id>/", views.deleteService),
    path("parts/edit/<int:id>/", views.editPart),
    path("parts/delete/<int:id>/", views.deletePart),
    path("orders/", views.listOrders),
    path("orders/add/", views.addOrder),
    path("orders/edit/<int:id>/", views.editOrder),
    path("orders/delete/<int:id>/", views.deleteOrder),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
