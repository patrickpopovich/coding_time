# Generated by Django 4.0.4 on 2022-07-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_estudiante_options_alter_trabajo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses'),
        ),
    ]