# Generated by Django 3.0.7 on 2020-08-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200802_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='handshape',
            name='sigml',
            field=models.TextField(default='<sigml></sigml>'),
        ),
    ]
