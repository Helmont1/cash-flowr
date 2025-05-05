from django.apps import AppConfig

class TransactionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.transactions"
    
    def ready(self):
        import utils.signals
        return super().ready()
