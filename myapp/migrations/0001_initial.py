# Generated by Django 4.1.3 on 2023-01-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('PhEmailone', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='img/%y')),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]