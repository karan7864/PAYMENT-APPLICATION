# Generated by Django 4.0.3 on 2022-04-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0009_loanapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='loantype',
            name='need_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='aadhar_image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='pan_image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='profile_photo',
            field=models.FileField(upload_to=''),
        ),
    ]
