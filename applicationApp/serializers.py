# serializers.py
from rest_framework import serializers
from .models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'date_of_birth', 'national_id', 'degree_or_diploma', 'status']