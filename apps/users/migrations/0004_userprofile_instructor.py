# Generated by Django 4.2.2 on 2023-06-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instructor',
            field=models.BooleanField(default=False),
        ),
    ]
