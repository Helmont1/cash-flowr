from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import BaseModel
import logging

logger = logging.getLogger(__name__)

@receiver(post_save)
@receiver(post_delete)
def log_model_changes(sender, instance, created=None, **kwargs):
    if issubclass(sender, BaseModel):
        if kwargs.get('created', False):
            logger.info(f'{sender.__name__} instance created: {instance} at {now()}')
        else:
            if kwargs.get('signal') == post_save:
                logger.info(f'{sender.__name__} instance updated: {instance} at {now()}')

        if kwargs.get('signal') == post_delete:
            logger.info(f'{sender.__name__} instance deleted: {instance} at {now()}')