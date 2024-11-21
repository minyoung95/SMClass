# Generated by Django 5.1.3 on 2024-11-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nicName', models.CharField(max_length=100)),
                ('tel', models.CharField(default='010-1111-1111', max_length=100)),
                ('gender', models.CharField(default='남자', max_length=30)),
                ('mdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
