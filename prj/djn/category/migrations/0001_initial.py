# Generated by Django 3.1.5 on 2021-01-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=256)),
                ('description_category', models.CharField(max_length=4096)),
            ],
        ),
    ]