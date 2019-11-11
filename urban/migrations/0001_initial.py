# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-11 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(default='default.jpg', upload_to='photos/')),
                ('description', models.TextField(default=22)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('travel', 'Travel'), ('food', 'Food'), ('places', 'Places'), ('people', 'People'), ('sports', 'Sports')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urban.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urban.Editor'),
        ),
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urban.Location'),
        ),
    ]
