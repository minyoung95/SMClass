# Generated by Django 5.1.3 on 2024-11-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hobby',
            field=models.CharField(default='No hobby', max_length=30),
            preserve_default=False,
        ),
    ]
