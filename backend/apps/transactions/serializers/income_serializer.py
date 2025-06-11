from rest_framework import serializers

from apps.transactions.models.income import Income

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'