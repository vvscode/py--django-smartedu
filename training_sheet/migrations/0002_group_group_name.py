# Generated by Django 3.0.5 on 2020-04-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_sheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_name',
            field=models.CharField(default='Undefined group name', max_length=300),
            preserve_default=False,
        ),
    ]