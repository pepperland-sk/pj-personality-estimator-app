# Generated by Django 2.2.5 on 2020-04-29 11:52

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, max_length=1000, null=True, verbose_name='post')),
                ('label', models.CharField(max_length=4, verbose_name='label')),
                ('score_ie', models.FloatField(default=0.0, verbose_name='score_ie')),
                ('score_sn', models.FloatField(default=0.0, verbose_name='score_sn')),
                ('score_tf', models.FloatField(default=0.0, verbose_name='score_tf')),
                ('score_pj', models.FloatField(default=0.0, verbose_name='score_pj')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'post',
                'db_table': 'post',
                'ordering': ['created_at'],
            },
        ),
    ]