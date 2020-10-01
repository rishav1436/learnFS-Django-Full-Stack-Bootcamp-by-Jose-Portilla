from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    Basic view of first Django Web App
    """
    return HttpResponse("<em> My Second App </em>")

def help(request):
    """
    renders the help view
    """
    context = {"page_title": "Help Page"}
    return render(request, "AppTwo/help.html", context=context)