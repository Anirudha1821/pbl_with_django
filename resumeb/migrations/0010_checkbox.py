# Generated by Django 4.2 on 2023-05-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeb', '0009_alter_f_dm1_alter_f_dm2'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userskils', models.CharField(max_length=300)),
            ],
        ),
    ]
