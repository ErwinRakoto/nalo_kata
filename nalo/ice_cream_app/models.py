from django.db import models
from rest_framework import serializers


class Ice(models.Model):
    savour = models.CharField(max_length=50)


class IceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('savour',)
        model = Ice


class IceBowl(models.Model):
    ice = models.ForeignKey(Ice, related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    scoop_number = models.PositiveIntegerField(default=40)


class IceBowlSerializer(serializers.ModelSerializer):
    ice = IceSerializer()

    class Meta:
        fields = '__all__'
        model = IceBowl


class Command(models.Model):
    order_command = models.CharField(max_length=50)
    ask_scoop_number = models.IntegerField()
    ice = models.ForeignKey(Ice, related_name='+', on_delete=models.SET_NULL, null=True, blank=True)


class CommandSerializer(serializers.ModelSerializer):
    ice = IceSerializer()

    class Meta:
        fields = '__all__'
        model = Command
