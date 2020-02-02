from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Char


@receiver(post_save, sender=Char)
def save_task(sender, instance, **kwargs):
    try:
        cache.delete("user")
    except Exception as err:
        print("Activity does not exist ", err)