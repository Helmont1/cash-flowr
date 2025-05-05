from django.urls import path, include
urlpatterns = [
    path('transactions/', include('apps.transactions.urls'))
]