# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=3, choices=[(b'MR', b'MR.'), (b'MRS', b'MRS.'), (b'MS', b'MS.'), (b'DR', b'DR.')])),
                ('Company_name', models.CharField(max_length=200, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.BigIntegerField(max_length=11)),
                ('time_frame', models.CharField(max_length=2, choices=[(b'1M', b'1 Month'), (b'3M', b'3 Months'), (b'6M', b'6 Months'), (b'1Y', b'1 Year'), (b'NS', b'Not Sure')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
