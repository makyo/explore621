# Generated by Django 2.1.3 on 2018-12-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181205_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_type',
            field=models.IntegerField(choices=[(0, 'general'), (1, 'artist'), (3, 'copyright'), (4, 'character'), (5, 'species')], default=-1),
        ),
    ]
