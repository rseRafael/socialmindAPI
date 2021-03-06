# Generated by Django 2.1.1 on 2018-09-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('startdate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('hasfinished', models.BooleanField(blank=True, null=True)),
                ('hasstarted', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
