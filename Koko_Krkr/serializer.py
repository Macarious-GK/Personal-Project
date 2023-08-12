from rest_framework import serializers
from Koko_Krkr.models import *


class friendserializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'