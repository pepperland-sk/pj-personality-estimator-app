# Generated by Django 2.2.5 on 2020-05-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbti',
            name='type',
            field=models.TextField(blank=True, null=True, verbose_name='type'),
        ),
    ]
