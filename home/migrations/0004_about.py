# Generated by Django 4.2.1 on 2023-06-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_blogs_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField()),
                ('Birthday', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('City', models.CharField(max_length=25)),
            ],
        ),
    ]
