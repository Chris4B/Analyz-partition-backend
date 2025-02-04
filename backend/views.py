from django.http import HttpResponse

def home(request):
    """ Simple homepage for the backend API """
    return HttpResponse("<h1>Welcome to Analyz Partition Backend</h1>")
