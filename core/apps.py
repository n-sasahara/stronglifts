from django.apps import AppConfig
from django.db.models.signals import post_migrate, post_save


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core.signals import create_default_exercises, create_user_profile
        from .models import User
        post_migrate.connect(create_default_exercises, sender=self)
        post_save.connect(create_user_profile, sender=User)