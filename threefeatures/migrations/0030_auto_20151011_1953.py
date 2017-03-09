# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0029_ucretsiz_hizmet_talepleri_ucretsiz_hizmetler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucretsiz_hizmetler',
            name='foto_video',
            field=models.FileField(verbose_name='Fotoğraf/Video', upload_to='ucretsizler/'),
        ),
    ]
