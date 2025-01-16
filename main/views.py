from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Portfolio!</h1><p>This is a showcase of my skills.</p>")
