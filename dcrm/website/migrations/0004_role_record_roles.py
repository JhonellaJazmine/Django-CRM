# Generated by Django 4.2.5 on 2023-10-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_brand_description_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='roles',
            field=models.ManyToManyField(related_name='records', to='website.role'),
        ),
    ]