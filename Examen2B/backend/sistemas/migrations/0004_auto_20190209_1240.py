# Generated by Django 2.1.5 on 2019-02-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemas', '0003_auto_20190205_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='numeroPastillas',
            field=models.IntegerField(),
        ),
    ]