# Generated by Django 4.2.1 on 2023-05-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_libro_fecha_lanzamiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidad_copias',
            field=models.PositiveIntegerField(default=100, verbose_name='número de copias'),
        ),
        migrations.AddField(
            model_name='libro',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.CharField(max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='paginas',
            field=models.PositiveIntegerField(),
        ),
    ]
