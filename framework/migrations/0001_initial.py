# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('crate_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbf\x9d\xe5\xad\x98\xe6\x97\xa5\xe6\x9c\x9f')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xa5\xe6\x9c\x9f')),
                ('owner', models.ForeignKey(related_name='framework_book_owner', verbose_name=b'owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
