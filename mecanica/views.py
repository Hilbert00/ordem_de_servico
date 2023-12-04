from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Client, Vehicle, Worker, Team, Part, Service, Order

@login_required
def home(request):     
    return render(request, "home.html")


@login_required
def addWorker(request):
    message = False
    
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        specialty = request.POST.get("specialty")
        salary = request.POST.get("salary")
        rg = request.POST.get("rg")
        team_id = request.POST.get("team_id")
                    
        if not name or not address or not specialty or not salary or not rg or not team_id or team_id == "0":
            message = {"type": "danger", "txt": "Preencha todos os campos!"}
        else:
            team = Team.objects.get(id=team_id)
            if team:
                Worker(name=name, address=address, specialty=specialty, salary=salary, rg=rg, team_id=team).save()
                return HttpResponseRedirect("/workers/add/?status=200")
    elif request.GET.get("status") == "200":
        message = {"type": "success", "txt": "Funcionário salvo com sucesso!"}

    teams = Team.objects.all()
    
    data = {
        "title": "Funcionários",
        "message": message,
        "fields": [
            {
                "name": "name",
                "label": "Nome:",
                "placeholder": "Insira o nome completo",
                "type": "input",
                "data": "text"
            },
            {
                "name": "address",
                "label": "Endereço:",
                "placeholder": "Insira o endereço",
                "type": "input",
                "data": "text"
            },
            {
                "name": "specialty",
                "label": "Especialidade:",
                "placeholder": "Insira a especialidade",
                "type": "input",
                "data": "text"
            },
            {
                "name": "salary",
                "label": "Salário:",
                "placeholder": "Insira o salário",
                "type": "input",
                "data": "number"
            },
            {
                "name": "rg",
                "label": "RG:",
                "placeholder": "Insira o RG",
                "type": "input",
                "data": "number"
            },
            {
                "name": "team_id",
                "label": "Equipe:",
                "placeholder": "Selecione a equipe",
                "type": "select",
                "data": teams
            }
        ]
    }
    return render(request, "add.html", data)


@login_required
def addVehicle(request):
    message = False
    
    if request.method == "POST":
        model = request.POST.get("model")
        brand = request.POST.get("brand")
        year = request.POST.get("year")
        plate = request.POST.get("plate")
        type = request.POST.get("type")
        client_id = request.POST.get("client_id")
                    
        if not model or not brand or not year or not plate or not type or not client_id or client_id == "0":
            message = {"type": "danger", "txt": "Preencha todos os campos!"}
        else:
            client = Client.objects.get(id=client_id)
            if client:
                Vehicle(model=model, brand=brand, year=year, plate=plate, type=type, client_id=client).save()
                return HttpResponseRedirect("/vehicles/add/?status=200")
    elif request.GET.get("status") == "200":
        message = {"type": "success", "txt": "Veículo salvo com sucesso!"}
    
    clients = Client.objects.all()
    
    data = {
        "title": "Veículos",
        "message": message,
        "fields": [
            {
                "name": "model",
                "label": "Modelo:",
                "placeholder": "Insira o modelo",
                "type": "input",
                "data": "text"
            },
            {
                "name": "brand",
                "label": "Marca:",
                "placeholder": "Insira a marca",
                "type": "input",
                "data": "text"
            },
            {
                "name": "plate",
                "label": "Placa:",
                "placeholder": "Insira a placa",
                "type": "input",
                "data": "text"
            },
            {
                "name": "year",
                "label": "Ano:",
                "placeholder": "Insira o ano",
                "type": "input",
                "data": "number"
            },
            {
                "name": "type",
                "label": "Tipo:",
                "placeholder": "Insira o tipo (Ex: carro, moto)",
                "type": "input",
                "data": "text"
            },
            {
                "name": "client_id",
                "label": "Cliente:",
                "placeholder": "Selecione o cliente",
                "type": "select",
                "data": clients
            }
        ]
    }
    return render(request, "add.html", data)


@login_required
def addClient(request):
    message = False
    
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        code = request.POST.get("code")
        rg = request.POST.get("rg")
                    
        if not name or not address or not phone or not code or not rg:
            message = {"type": "danger", "txt": "Preencha todos os campos!"}
        else:
            Client(name=name, address=address, phone=phone, code=code, rg=rg).save()
            return HttpResponseRedirect("/clients/add/?status=200")
    elif request.GET.get("status") == "200":
        message = {"type": "success", "txt": "Cliente salvo com sucesso!"}
    
    data = {
        "title": "Clientes",
        "message": message,
        "fields": [
            {
                "name": "name",
                "label": "Nome:",
                "placeholder": "Insira o nome completo",
                "type": "input",
                "data": "text"
            },
            {
                "name": "address",
                "label": "Endereço:",
                "placeholder": "Insira o endereço",
                "type": "input",
                "data": "text"
            },
            {
                "name": "phone",
                "label": "Telefone:",
                "placeholder": "Insira o número de telefone",
                "type": "input",
                "data": "text"
            },
            {
                "name": "code",
                "label": "Código:",
                "placeholder": "Insira o código",
                "type": "input",
                "data": "text"
            },
            {
                "name": "rg",
                "label": "RG:",
                "placeholder": "Insira o RG",
                "type": "input",
                "data": "number"
            }
        ]
    }
    return render(request, "add.html", data)


@login_required
def addService(request):
    message = False
    
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        description = request.POST.get("description")
        price = request.POST.get("price")
        type = request.POST.get("type")
        storage = request.POST.get("storage")
                    
        if not name or not price or not description or not price or not type or type == "0":
            message = {"type": "danger", "txt": "Preencha todos os campos!"}
        else:
            if type == "1" and not storage:
                message = {"type": "danger", "txt": "Preencha todos os campos!"}
            else:
                if type == "1":
                    Part(name=name, code=code, description=description, price=price, storage=storage).save()
                else:
                    Service(name=name, code=code, description=description, price=price).save()
                return HttpResponseRedirect("/services/add/?status=200")
    elif request.GET.get("status") == "200":
        message = {"type": "success", "txt": "Serviço/Peça salva com sucesso!"}
    
    
    data = {
        "title": "Peças e Serviços",
        "message": message,
        "fields": [
            {
                "name": "name",
                "label": "Nome:",
                "placeholder": "Insira o nome",
                "type": "input",
                "data": "text"
            },
            {
                "name": "type",
                "label": "Tipo:",
                "placeholder": "Selecione o tipo",
                "type": "select",
                "data": [
                    {
                        "id": 1,
                        "name": "Peça"
                    },
                    {
                        "id": 2,
                        "name": "Serviço"
                    }
                ]
            },
            {
                "name": "code",
                "label": "Código:",
                "placeholder": "Insira o código",
                "type": "input",
                "data": "text"
            },
            {
                "name": "description",
                "label": "Descrição:",
                "placeholder": "Insira a descrição",
                "type": "input",
                "data": "text"
            },
            {
                "name": "price",
                "label": "Preço:",
                "placeholder": "Insira o preço unitário",
                "type": "input",
                "data": "text"
            },
            {
                "name": "storage",
                "label": "Estoque:",
                "placeholder": "Insira a quantidade em estoque (ignore se for um serviço)",
                "type": "input",
                "data": "number"
            }
        ]
    }
    return render(request, "add.html", data)


@login_required
def addOrder(request):
    message = False
    
    if request.method == "POST":
        team_id = request.POST.get("team_id")
        vehicle_id = request.POST.get("vehicle_id")
        conclusion_date = request.POST.get("conclusion_date")
        services = request.POST.getlist("services")
        parts = request.POST.getlist("parts")
                
        if not team_id or not vehicle_id or not conclusion_date or (len(services) == 0 and len(parts) == 0):
            message = {"type": "danger", "txt": "Preencha todos os campos!"}
        else:
            team = Team.objects.get(id=team_id)
            vehicle = Vehicle.objects.get(id=vehicle_id)
            partsToSave = []
            servicesToSave = []
            price = 0
            
            if team and vehicle:
                for service in services:
                    s = Service.objects.get(id=int(service))
                    
                    if s:
                        price += s.price
                        servicesToSave.append(s)
                        
                for part in parts:
                    p = Part.objects.get(id=int(part))
                    
                    if p:
                        price += p.price
                        partsToSave.append(p)
                
                if not len(partsToSave) and not len(servicesToSave) or price == 0:
                    message = {"type": "danger", "txt": "Um erro inesperado ocorreu!"}
                else:
                    order = Order(team_id=team, vehicle_id=vehicle, conclusion_date=conclusion_date, price=price)
                    order.save()
                    
                    for service in servicesToSave:
                        order.services.add(service)
                            
                    for part in partsToSave:
                        order.parts.add(part)

                    return HttpResponseRedirect("/orders/add/?status=200")  
            else:
                message = {"type": "danger", "txt": "Um erro inesperado ocorreu!"}               
    elif request.GET.get("status") == "200":
        message = {"type": "success", "txt": "Ordem de Serviço criada com sucesso!"}
    
    teams = Team.objects.all()
    vehicles = Vehicle.objects.all()
    servicesData = Service.objects.all()
    partsData = Part.objects.all()
    
    data = {
        "title": "Ordens de Serviço",
        "message": message,
        "fields": [
            {
                "name": "vehicle_id",
                "label": "Veículo:",
                "placeholder": "Selecione o veículo",
                "type": "select",
                "data": vehicles
            },
            {
                "name": "team_id",
                "label": "Equipe:",
                "placeholder": "Selecione a equipe",
                "type": "select",
                "data": teams
            },
            {
                "name": "services",
                "label": "Serviço(s):",
                "placeholder": "Selecione o(s) serviço(s)",
                "type": "select multiple",
                "data": servicesData
            },
            {
                "name": "parts",
                "label": "Peça(s):",
                "placeholder": "Selecione a(s) peça(s)",
                "type": "select multiple",
                "data": partsData
            },
            {
                "name": "conclusion_date",
                "label": "Data de conclusão:",
                "placeholder": "Insira a data de conclusão",
                "type": "input",
                "data": "date"
            }
        ]
    }
    return render(request, "add.html", data)


@login_required
def listWorkers(request):
    data = {"data": [{
        "title": "Funcionários",
        "data": fields(Worker, ["ID", "Equipe", "Salário", "Nome", "Especialidade", "Endereço", "RG"]),
    }]}    
                
    return render(request, "list.html", data)


@login_required
def listVehicles(request):
    data = {"data": [{
        "title": "Veículos",
        "data": fields(Vehicle, ["ID", "Cliente", "Modelo", "Marca", "Ano", "Placa", "Tipo"]),
    }]}
                
    return render(request, "list.html", data)


@login_required
def listClients(request):
    data = {"data": [{
        "title": "Clientes",
        "data": fields(Client, ["ID", "Nome", "Endereço", "Telefone", "Código", "RG"]),
    }]}
                
    return render(request, "list.html", data)


@login_required
def listServices(request):
    data = {"data": [
        {
        "title": "Peças",
        "data": fields(Part, ["ID", "Nome", "Código", "Estoque", "Descrição", "Preço"]),
        },
        {
        "title": "Serviços",
        "data": fields(Service, ["ID", "Nome", "Código", "Descrição", "Preço"]),
        }
    ]}
                
    return render(request, "list.html", data)


@login_required
def listOrders(request):
    data = {"data": [{
        "title": "Ordens de Serviço",
        "data": fields(Order, ["ID", "Equipe", "Veículo", "Preço", "Realizada em", "Prazo de conclusão", "Serviços", "Peças"]),
    }]}
                
    return render(request, "list.html", data)


def fields(model, names):
    elements = model.objects.all()
    
    def get_name(e):
        return e.name
    
    
    def remove_order(e):
        if e == "order" or e == "vehicle":
            return False
        
        return True
    
    
    modelFields = list(filter(remove_order, list(list(map(get_name, model._meta.get_fields())))))
    modelView = []    
    
    for element in elements:
        data = []
        for index, field in enumerate(modelFields):
            if field == "services":
                value = "".join(list(map(get_name, element.services.all())))
            elif field == "parts":
                value = ", ".join(list(map(get_name, element.parts.all())))
            else:
                try:
                    value = getattr(element, field)
                    value = str(value).split(" from ")[0]
                except:
                    value = getattr(element, field)
                
            data.append({"name": names[index], "value": value})
        
        modelView.append(data)
        
    return modelView
