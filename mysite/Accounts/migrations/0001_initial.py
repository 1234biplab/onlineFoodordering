# Generated by Django 2.2 on 2019-04-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('status', models.CharField(default='Active', max_length=10)),
            ],
        ),
    ]