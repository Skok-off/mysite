# Generated by Django 2.1.dev20180414005831 on 2018-04-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('post', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
