from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    code = models.CharField(max_length=5)
    rg = models.CharField(max_length=7)
    
    def __str__(self):
        return f"{self.name} from Clients"
    
    
class Vehicle(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    model = models.CharField(max_length=45)
    brand = models.CharField(max_length=45)
    year = models.IntegerField()
    plate = models.CharField(max_length=8)
    type = models.CharField(max_length=45)
    
    def __str__(self):
        return f"{self.model} - {self.plate} from Vehicles"
 

class Team(models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return f"{self.name} from Teams"
 
 
class Worker(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=45)
    specialty = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    rg = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name} from Workers"
    
    
class Service(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=5)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} from Services"
    
    
class Part(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=5)
    storage = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} from Parts"
    
    
class Order(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateField(auto_now_add=True)
    conclusion_date = models.DateField()
    services = models.ManyToManyField(Service, related_name="orders")
    parts = models.ManyToManyField(Part, related_name="orders")

    def __str__(self):
        return f"{self.vehicle_id} - {self.team_id} from Service Orders"
