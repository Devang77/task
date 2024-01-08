# Generated by Django 4.2.3 on 2024-01-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, unique=True)),
                ('customer_number', models.CharField(max_length=100, unique=True)),
                ('customer_address', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
    ]