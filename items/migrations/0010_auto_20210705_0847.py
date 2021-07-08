# Generated by Django 3.2.3 on 2021-07-05 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20210628_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='items.tema'),
        ),
    ]
