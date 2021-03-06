# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descricao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_descricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.IntegerField()),
                ('condominio', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=300)),
                ('liberacao', models.CharField(max_length=200)),
                ('data_liberacao', models.DateField()),
                ('nome_operador', models.CharField(max_length=200)),
                ('central', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
