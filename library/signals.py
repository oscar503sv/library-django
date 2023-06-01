from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import Perfil

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    group_names = ['admin', 'bibliotecario','usuario']  # Aquí puedes añadir los nombres de los grupos que deseas crear

    for group_name in group_names:
        Group.objects.get_or_create(name=group_name)

# Registra la función de creación de grupos por defecto con la señal post_migrate
post_migrate.connect(create_default_groups)

@receiver(post_save, sender=Perfil)
def add_user_to_admin_group(sender, instance, created, **kwargs):
    if created:
        try:
            admin = Group.objects.get(name='admin')
        except Group.DoesNotExist:
            admin = Group.objects.create(name='admin')
        instance.usuario.groups.add(admin)
