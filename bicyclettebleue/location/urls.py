
from django.urls import path, include
from . import views

app_name = 'location'

urlpatterns = [
    path('',views.location, name='index'),
    path('<int:id>/', views.detailsLocation, name='detailsLocation'),
    path('nouvelleLocation/', views.nouvelleLocation, name='nouvelleLocation'),
    path('modifierLocation/<str:pk>', views.modifierlocation, name='modifierLocation'),
    path('supprimerLocation/<str:pk>',views.supprimerLocation, name='supprimerLocation'),
]
