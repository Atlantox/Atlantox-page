# Generated by Django 4.1.3 on 2022-11-15 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Briefcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Título')),
                ('img', models.ImageField(upload_to='briefcase/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Portafolio',
                'verbose_name_plural': 'Portafolios',
            },
        ),
    ]