from django.core.validators import EmailValidator
from rest_framework import serializers

from Contactos.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    ContactSerializer is used for validating and processing incoming data from API requests.
    """
    name = serializers.CharField(max_length=80, required=True)
    first_surname = serializers.CharField(max_length=80, required=False)
    second_surname = serializers.CharField(max_length=80, required=False)
    phone = serializers.CharField(max_length=15, required=True)
    email = serializers.EmailField(required=False, validators=(EmailValidator,))

    class Meta:
        model = Contact
        fields = (
            'id',
            'name',
            'first_surname',
            'second_surname',
            'phone',
            'email',
            'created_at',
            'updated_at'
        )
