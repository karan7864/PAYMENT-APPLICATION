# Generated by Django 4.0.3 on 2022-04-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0004_loancategory_loantype'),
    ]

    operations = [
        migrations.AddField(
            model_name='loantype',
            name='loan_image',
            field=models.ImageField(default='a.jpg', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
