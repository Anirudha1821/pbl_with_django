# Generated by Django 4.2 on 2023-05-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='F',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=32)),
                ('dsurname', models.CharField(max_length=32)),
                ('dpincode', models.CharField(max_length=32)),
                ('dcity', models.CharField(max_length=32)),
                ('dcountry', models.CharField(max_length=32)),
                ('dphoneno', models.IntegerField()),
                ('demail', models.CharField(max_length=323)),
                ('desc', models.CharField(max_length=323)),
                ('dschool', models.CharField(max_length=323)),
                ('dposition', models.CharField(max_length=323)),
                ('dcompany', models.CharField(max_length=323)),
                ('dc1', models.CharField(max_length=323)),
                ('dcc1', models.CharField(max_length=323)),
                ('dm1', models.CharField(max_length=323)),
                ('dm2', models.CharField(max_length=323)),
                ('dcollege', models.TextField()),
                ('ddegree', models.TextField()),
                ('dmonth', models.TextField()),
            ],
        ),
    ]
