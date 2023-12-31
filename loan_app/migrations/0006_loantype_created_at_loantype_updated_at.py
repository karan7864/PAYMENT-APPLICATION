# Generated by Django 4.0.3 on 2022-04-03 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0005_loantype_loan_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='loantype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loantype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
