# Generated by Django 4.2.3 on 2023-07-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Mail', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
