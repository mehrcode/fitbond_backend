from rest_framework import serializers
from account.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userfields = ['email', 'date_joined']