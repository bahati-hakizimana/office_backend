# Generated by Django 5.0.6 on 2024-09-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('staff', 'Staff')], default='user', max_length=10),
        ),
    ]
