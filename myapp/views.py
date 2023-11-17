from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def hello(request):
    
    return HttpResponse("<h1>Hello</h1>")
