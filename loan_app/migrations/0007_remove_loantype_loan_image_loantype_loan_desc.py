# Generated by Django 4.0.3 on 2022-04-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0006_loantype_created_at_loantype_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loantype',
            name='loan_image',
        ),
        migrations.AddField(
            model_name='loantype',
            name='loan_desc',
            field=models.TextField(default='A', max_length=1000),
            preserve_default=False,
        ),
    ]