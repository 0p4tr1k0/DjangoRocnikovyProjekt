from django.shortcuts import render
from myfirst.models import Tank
from django.views.generic import ListView, DetailView


def index(request):
    tanks = Tank.objects.all().order_by('nations')[:3]
    context={
        "tanks":tanks
    }
    return render(request, 'index.html', context=context)

class TankListView(ListView):
 # Nastavení požadovaného modelu
 model = Tank
 context_object_name = 'tank_list'
 # Umístění a název šablony
 template_name = 'list.html'

class TankDetailView(DetailView):
 # Nastavení požadovaného modelu
 model = Tank
 context_object_name = 'tank_detail'
 # Umístění a název šablony
 template_name = 'detail.html'