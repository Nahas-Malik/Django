from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the One-to-Field app!</h1>")
