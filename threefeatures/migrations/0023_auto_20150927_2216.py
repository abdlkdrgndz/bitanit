# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threefeatures', '0022_auto_20150926_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('kullanici_ip', models.GenericIPAddressField()),
                ('kullanici_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kullanıcı Profili',
                'verbose_name_plural': 'Kullanıcı Profilleri',
            },
        ),
        migrations.AlterModelOptions(
            name='abonelik',
            options={'verbose_name': 'E-Posta Adresi', 'verbose_name_plural': 'E-Posta Adres'},
        ),
    ]
