# Generated by Django 3.2.5 on 2021-07-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumda', '0002_comment_diary_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='block',
            field=models.BooleanField(default=False),
        ),
    ]