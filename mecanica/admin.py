from .models import Client, Vehicle, Worker, Team, Part, Service, Order
from django.contrib import admin

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(Worker)
admin.site.register(Team)
admin.site.register(Part)
admin.site.register(Service)
admin.site.register(Order)
