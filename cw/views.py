from django.shortcuts import render
from django.db.models import Q
from .models import *
from .forms import *


def index(request):
    data = UserModel.objects.all()

    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def create_user(request):
    form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)
