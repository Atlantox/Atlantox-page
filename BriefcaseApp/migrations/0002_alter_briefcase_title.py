# Generated by Django 4.1.3 on 2022-11-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BriefcaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='briefcase',
            name='title',
            field=models.CharField(max_length=55, verbose_name='Título'),
        ),
    ]
