# Generated by Django 4.0.6 on 2022-08-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_userprofile_date_of_birth_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Date_of_birth',
            new_name='dob',
        ),
    ]
