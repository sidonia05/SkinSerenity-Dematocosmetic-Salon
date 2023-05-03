from django.shortcuts import render
from .models import Services

def services(request):
    services = Services.objects.all()
    return render(request, 'tarife/tarife.html', {'service': services})
