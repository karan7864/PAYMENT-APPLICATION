# Generated by Django 4.0.3 on 2022-04-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0014_loanapplication_rejected_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='payment_schedule',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
