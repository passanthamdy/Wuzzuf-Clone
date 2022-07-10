from dataclasses import fields
from accounts.serializers import CompanySerializer, EmployeeSerializer
from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    company=CompanySerializer
    reviewer=EmployeeSerializer
    class Meta:
        model=Review
        fields="__all__"
        

class UpdateReviewSerializer(serializers.ModelSerializer):
    company=CompanySerializer
    reviewer=EmployeeSerializer
    class Meta:
        model=Review
        fields=["reviewer","company","pros","cons","employment_status","rating","is_published"]
        optional_fields=["reviewer","company","pros","cons","employment_status","rating","is_published"]

                