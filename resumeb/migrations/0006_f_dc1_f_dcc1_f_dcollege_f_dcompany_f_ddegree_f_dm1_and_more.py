# Generated by Django 4.2 on 2023-05-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeb', '0005_remove_f_dc1_remove_f_dcc1_remove_f_dcollege_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='f',
            name='dc1',
            field=models.CharField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='dcc1',
            field=models.CharField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='dcollege',
            field=models.TextField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='dcompany',
            field=models.CharField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='ddegree',
            field=models.TextField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='dm1',
            field=models.IntegerField(default=9),
        ),
        migrations.AddField(
            model_name='f',
            name='dm2',
            field=models.IntegerField(default=8),
        ),
        migrations.AddField(
            model_name='f',
            name='dmonth',
            field=models.CharField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='dposition',
            field=models.CharField(default='aj', max_length=323),
        ),
        migrations.AddField(
            model_name='f',
            name='dschool',
            field=models.CharField(default='aj', max_length=323),
        ),
    ]
