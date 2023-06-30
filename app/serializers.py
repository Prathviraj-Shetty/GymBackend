from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Gym,Client,Slot,Trainer,Booking
# from .models import 


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



