# Generated by Django 2.2 on 2019-04-18 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190418_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='favoriteAnimal',
            new_name='favorite_animal',
        ),
    ]