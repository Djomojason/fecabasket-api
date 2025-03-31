from django.shortcuts import render
from rest_framework import viewsets
from .models import Club, Entraineur, Joueur, Officiel
from .serializers import ClubSerializer, EntraineurSerializer, JoueurSerializer, OfficielSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class EntraineurViewSet(viewsets.ModelViewSet):
    queryset = Entraineur.objects.all()
    serializer_class = EntraineurSerializer

class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer

    def create(self, request, *args, **kwargs):
        print("Données reçues:", request.data)  # Debug
        return super().create(request, *args, **kwargs)

class OfficielViewSet(viewsets.ModelViewSet):
    queryset = Officiel.objects.all()
    serializer_class = OfficielSerializer

#python manage.py runserver         