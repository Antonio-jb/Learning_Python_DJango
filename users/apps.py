from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # Nombre que saldra en la interface de la app
    verbose_name = 'Usuarios'
