# Generated by Django 3.2.3 on 2021-06-30 14:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20210628_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]