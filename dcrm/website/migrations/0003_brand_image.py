# Generated by Django 4.2.5 on 2023-10-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_role_user_name_alter_user_email_user_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='image-svgrepo-com.svg', null=True, upload_to=''),
        ),
    ]
