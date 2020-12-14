from rest_framework import serializers

from .models import Checklist


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ('id', 'name', 'description')
        read_only_fields = fields