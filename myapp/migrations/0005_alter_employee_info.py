# Generated by Django 3.2.2 on 2021-06-07 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_employee_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.employinfo'),
        ),
    ]
