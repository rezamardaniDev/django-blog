# Generated by Django 5.1.4 on 2025-01-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_view',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
