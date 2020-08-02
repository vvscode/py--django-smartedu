# Generated by Django 3.0.8 on 2020-07-18 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("training_sheet", "0003_auto_20200718_0539"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="groups",
                to="training_sheet.Course",
            ),
        ),
    ]