# Generated by Django 2.2 on 2019-04-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
