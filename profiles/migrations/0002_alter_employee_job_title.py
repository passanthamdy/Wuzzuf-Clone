# Generated by Django 4.0.5 on 2022-07-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
