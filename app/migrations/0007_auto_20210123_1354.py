# Generated by Django 3.1.5 on 2021-01-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_commenttoarticle_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttoarticle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
