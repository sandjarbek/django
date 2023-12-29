from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def homepage(request):

    context = {"name": "Sanjar"}
    return render(request, 'crm/index.html', context)
def register(request):
    return render(request, 'crm/register.html')


