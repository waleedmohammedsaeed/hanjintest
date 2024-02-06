# Generated by Django 5.0.1 on 2024-01-28 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=60)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serName', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('categeory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]