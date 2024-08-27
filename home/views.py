from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("<h1> Hello world</h1>")



def index(request):
    # using dictionaries
    context = {
        "name": "nipun is learning django",
        "name1": "from code with harry",
        }
    return render(request,"index.html", context)
    #return HttpResponse("welcome to nipun webpage")

def contact(request):
    # return render(request, 'about.html')
    return HttpResponse("sakhu west pendam")

def events(request):
    return render(request, 'services.html')
    # return HttpResponse("event starting on 11th sept")

def ravongla_star(request):
    return render(request,'ravongla_star.html')