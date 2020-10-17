from django.http import request
from django.shortcuts import render, redirect
from .models import *
from .forms import tambahForm

def schedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'story5/form.html', {'schedule':schedule})

def matkul(request, param):
    schedule = Schedule.objects.get(matkul=param)
    return render(request, 'story5/form.html', {'schedule':schedule})

def tambah(request):
    form = tambahForm()

    if request.method == 'POST':
        form = tambahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/story5/story5")

    context = {'form':form}
    return render(request, 'story5/tambah.html', context)

def update(request, param):
    schedule = Schedule.objects.get(id = param)
    form = tambahForm(instance=schedule)

    if request.method == 'POST':
        form = tambahForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect("/story5/story5")

    context = {'form':form}
    return render(request, 'story5/tambah.html', context)

def hapus(request, param):
    schedule = Schedule.objects.filter(id = param)
    matkul = Schedule.objects.get(id = param)
    if request.method == 'POST':
        schedule.delete()
        return redirect("/story5/story5")

    context = {'matkul':matkul}
    return render(request, 'story5/hapus.html', context)

def details(request, param):
    schedule = Schedule.objects.get(id = param)
    context = {'schedule':schedule}
    return render(request, 'story5/detail.html', context)