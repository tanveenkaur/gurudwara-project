# Generated by Django 2.0.2 on 2020-08-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FORM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.CharField(default='SOME STRING', max_length=16),
        ),
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.CharField(editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]
