# Generated by Django 3.2.5 on 2021-07-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumda', '0003_diary_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='title',
            field=models.CharField(default='title', max_length=100, verbose_name='일기 제목'),
            preserve_default=False,
        ),
    ]
