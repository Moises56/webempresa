# Generated by Django 4.0.1 on 2022-01-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.TextField(verbose_name='Descripción')),
                ('content', models.CharField(max_length=200, verbose_name='Sub-Titulo')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-created_at'],
            },
        ),
    ]
