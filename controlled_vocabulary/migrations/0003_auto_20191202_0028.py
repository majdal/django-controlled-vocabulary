# Generated by Django 2.2.7 on 2019-12-02 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlled_vocabulary', '0002_auto_20191201_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlledterm',
            name='definition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='controlledvocabulary',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
