# Generated by Django 4.0.3 on 2022-04-03 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0003_auto_20220402_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=200)),
                ('max_loan_amount', models.FloatField()),
                ('loan_roi', models.FloatField()),
                ('max_loan_duration', models.CharField(max_length=4)),
                ('loan_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_app.loancategory')),
            ],
        ),
    ]
