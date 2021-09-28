from django import forms
from.models import Location_Velo
from.models import Location
from.models import Client

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('loc_id', 'loc_statut', 'loc_client')

class LocationVeloForm(forms.ModelForm):
    class Meta:
        model = Location_Velo
        fields = ('date_debut', 'date_fin', 'lv_vel_id')

