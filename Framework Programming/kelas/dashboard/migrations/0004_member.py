# Generated by Django 2.2.12 on 2022-11-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20221101_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('join_date', models.CharField(max_length=50)),
            ],
        ),
    ]