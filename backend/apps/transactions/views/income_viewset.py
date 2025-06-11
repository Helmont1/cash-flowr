from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.transactions.models.income import Income
from apps.transactions.serializers.income_serializer import IncomeSerializer

class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    
    async def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data) if self.paginator else Response(serializer.data)
    
    async def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)