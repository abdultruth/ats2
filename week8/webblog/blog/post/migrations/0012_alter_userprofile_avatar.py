# Generated by Django 4.0.6 on 2022-08-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default.jfif', upload_to='media'),
        ),
    ]
