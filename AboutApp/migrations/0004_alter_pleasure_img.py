# Generated by Django 4.1.3 on 2022-11-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutApp', '0003_alter_pleasure_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pleasure',
            name='img',
            field=models.ImageField(default='NULL', null=True, upload_to='about', verbose_name='Imagen'),
        ),
    ]
