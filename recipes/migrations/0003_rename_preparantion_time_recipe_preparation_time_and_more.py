# Generated by Django 5.0.1 on 2024-05-06 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_author_alter_recipe_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_time',
            new_name='preparation_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_time_unit',
            new_name='preparation_time_unit',
        ),
    ]
