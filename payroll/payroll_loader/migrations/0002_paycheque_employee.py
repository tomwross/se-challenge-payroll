# Generated by Django 2.0.4 on 2018-04-23 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_loader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paycheque',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='payroll_loader.Employee'),
            preserve_default=False,
        ),
    ]
