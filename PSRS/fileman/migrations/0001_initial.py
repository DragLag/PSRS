# Generated by Django 3.1.7 on 2021-03-13 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
