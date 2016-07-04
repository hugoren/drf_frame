# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0003_auto_20160612_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(related_name='framework_book_owner', verbose_name=b'owner', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
