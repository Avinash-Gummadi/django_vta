# Generated by Django 4.0 on 2022-04-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadquestion',
            name='answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50),
        ),
    ]