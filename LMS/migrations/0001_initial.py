# Generated by Django 3.1.6 on 2022-04-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=50)),
                ('publication', models.CharField(max_length=50)),
                ('admin_email', models.EmailField(max_length=30)),
            ],
        ),
    ]
