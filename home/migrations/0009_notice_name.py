# Generated by Django 3.1.4 on 2020-12-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
