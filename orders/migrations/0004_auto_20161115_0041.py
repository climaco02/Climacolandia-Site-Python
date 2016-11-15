# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20161115_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersconcluded',
            name='concluded',
        ),
        migrations.AddField(
            model_name='ordersconcluded',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordersconcluded',
            name='type_sweet',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
