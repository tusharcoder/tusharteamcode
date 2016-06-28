# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('sal', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='firstname',
        ),
        migrations.DeleteModel(
            name='lastname',
        ),
        migrations.DeleteModel(
            name='salary',
        ),
    ]
