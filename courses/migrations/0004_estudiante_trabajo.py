# Generated by Django 4.0.4 on 2022-06-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courses_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
                ('last_name', models.CharField(max_length=69)),
                ('identification', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
                ('delivered', models.BooleanField(default=False)),
            ],
        ),
    ]
