from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def inscriptionPage(request):
    form = InscriptionForm()
    if request.method=='POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Compte crée avec succès pour ' + user)
            return redirect('/compte/login')
    context={
        'form' : form
    }
    return render(request, 'compte/inscription.html', context)


def loginPage(request):
    context={

    }
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Nom d'utilisateur et/ou mot de passe erroné")


    return render(request, 'compte/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/compte/login')
