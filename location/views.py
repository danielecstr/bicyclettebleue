from django.shortcuts import render,redirect
from .models import Location
from .models import Client
from .models import Location_Velo
from .forms import LocationForm
from .forms import LocationVeloForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/compte/login')
def location(request):
    location = Location.objects.all()
    locationvelo = Location_Velo.objects.all()
    location_number = location.count()
    messageNbLocation = f'{location_number} locations :'

    if location_number == 1:
        messageNbLocation = f'{location_number} location :'


    context = {
        'location' : location,
        'messageNbLocation' : messageNbLocation,
        'locationvelo': locationvelo,
    }

    return render(request, 'location/location.html', context)

@login_required(login_url='/compte/login')
def detailsLocation(request, id):
    locationvelo = Location_Velo.objects.get(id=id)
    messageDescriptionVelo = f"Il n'y a pas de remarque"

    if locationvelo.lv_vel_id.vel_remarque is not None :
        messageDescriptionVelo = locationvelo.lv_vel_id.vel_remarque



    context = {
        'locationvelo' : locationvelo,
        'messageDescriptionVelo' : messageDescriptionVelo
    }
    return render(request, 'location/detailsLocation.html', context)

@login_required(login_url='/compte/login')
def nouvelleLocation(request):
    formLocationVelo = LocationVeloForm()
    formLocation = LocationForm()
    if request.method=='POST':
        formLocation=LocationForm(request.POST)
        formLocationVelo = LocationVeloForm(request.POST)
        if formLocation.is_valid() and formLocationVelo.is_valid():
            formLocation.save()
            nbmax = Location.objects.latest('loc_id').loc_id
            locaVelo = Location_Velo(date_fin=formLocationVelo.cleaned_data.get('date_fin'), date_debut=formLocationVelo.cleaned_data.get('date_debut'),lv_loc_id_id=nbmax, id=nbmax,lv_vel_id_id=formLocationVelo.cleaned_data.get('lv_vel_id').vel_id)
            locaVelo.save()
            return redirect('/location')

    context = {
        'formLocation' : formLocation,
        'formLocationVelo' : formLocationVelo,
    }
    return render(request, 'location/nouvelleLocation.html', context)

@login_required(login_url='/compte/login')
def modifierlocation(request, pk):
    location = Location.objects.get(loc_id=pk)
    formLocation=LocationForm(instance=location)
    location2 = Location_Velo.objects.get(id=pk)
    formLocationVelo = LocationVeloForm(instance=location2)

    if request.method=='POST':
        formLocation=LocationForm(request.POST, instance=location)
        formLocationVelo=LocationVeloForm(request.POST, instance=location2)
        if formLocation.is_valid() and formLocationVelo.is_valid():
            formLocation.save()
            formLocationVelo.save()
            return redirect('/location')
    context = {
        'formLocation' : formLocation,
        'formLocationVelo' : formLocationVelo
    }
    return render(request, 'location/nouvelleLocation.html', context)

@login_required(login_url='/compte/login')
def supprimerLocation(request, pk):
    location = Location.objects.get(loc_id=pk)
    if request.method=='POST':
        location.delete()
        return redirect('/location')

    context = {
        'item': location,
    }
    return render(request, 'location/supprimerLocation.html', context)


