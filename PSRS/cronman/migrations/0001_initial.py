# Generated by Django 3.1.7 on 2021-03-13 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fileman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_string', models.CharField(max_length=200)),
                ('cron_date', models.DateTimeField(auto_now_add=True)),
                ('egg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileman.file')),
            ],
        ),
    ]