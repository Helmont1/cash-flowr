from rest_framework import serializers

from apps.transactions.models.expense import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'