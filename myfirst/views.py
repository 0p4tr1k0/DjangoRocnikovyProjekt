from django.shortcuts import render
from myfirst.models import Tank


def index(request):
    tanks = Tank.objects.all()
    context={
        "tanks":tanks
    }
    return render(request, 'index.html', context=context)
