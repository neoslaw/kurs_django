# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20141209_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(max_length=17, blank=True),
            preserve_default=True,
        ),
    ]
