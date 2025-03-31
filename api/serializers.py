from rest_framework import serializers
from .models import Club, Entraineur, Joueur, Officiel

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class EntraineurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entraineur
        fields = '__all__'

class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueur
        fields = '__all__'
        extra_kwargs = {
            'imc': {'read_only': True}  
        }

class OfficielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officiel
        fields = '__all__'

#python manage.py runserver        