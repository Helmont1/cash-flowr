from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.transactions.views.income_viewset import IncomeViewSet

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet, basename='income')

urlpatterns = router.urls