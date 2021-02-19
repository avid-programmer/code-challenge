from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['phone_no', 'password']
        extra_kwargs = {
                'password': {'write_only': True}
        }


