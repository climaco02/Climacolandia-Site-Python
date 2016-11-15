# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_concluded'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersConcluded',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concluded', models.ForeignKey(related_name='concluded', to='orders.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='order',
            name='concluded',
        ),
    ]
