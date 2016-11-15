# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='concluded',
            field=models.ManyToManyField(related_name='concluded_rel_+', to='orders.Order'),
            preserve_default=True,
        ),
    ]
