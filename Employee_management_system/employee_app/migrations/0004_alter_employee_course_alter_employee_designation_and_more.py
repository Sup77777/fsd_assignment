# Generated by Django 5.1.4 on 2024-12-20 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0003_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='course',
            field=models.CharField(choices=[('MCA', 'MCA'), ('AIML', 'AIML')], default='SELECT', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(choices=[('HR', 'HR'), ('Manager', 'Manager'), ('Sales', 'Sales')], default='SELECT', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='SELECT', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
    ]