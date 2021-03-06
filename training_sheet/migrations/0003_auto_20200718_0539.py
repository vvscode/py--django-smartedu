# Generated by Django 3.0.8 on 2020-07-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("training_sheet", "0002_applicationfortraining"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_teachers",
            field=models.ManyToManyField(blank=True, to="training_sheet.Teacher"),
        ),
        migrations.AlterField(
            model_name="course",
            name="tags",
            field=models.ManyToManyField(blank=True, to="training_sheet.Tag"),
        ),
        migrations.AlterField(
            model_name="group",
            name="group_teachers",
            field=models.ManyToManyField(blank=True, to="training_sheet.Teacher"),
        ),
        migrations.AlterField(
            model_name="group",
            name="students",
            field=models.ManyToManyField(blank=True, to="training_sheet.Student"),
        ),
    ]
