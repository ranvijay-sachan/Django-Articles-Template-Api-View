# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('hero_image', models.ImageField(upload_to=b'pic_folder/')),
                ('additional_image', models.ImageField(upload_to=b'pic_folder/')),
            ],
            options={
                'db_table': 'article',
            },
            bases=(models.Model,),
        ),
    ]
