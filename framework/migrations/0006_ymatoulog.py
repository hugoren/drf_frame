# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0005_auto_20160612_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='YMATOULOG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operater', models.CharField(max_length=200)),
                ('app', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbf\x9d\xe5\xad\x98\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
        ),
    ]
