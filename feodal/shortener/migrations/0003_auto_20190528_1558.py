# Generated by Django 2.2.1 on 2019-05-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20190528_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmap',
            name='full_url',
            field=models.TextField(),
        ),
    ]
