# Generated by Django 4.1.3 on 2023-01-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contact_alter_projects_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
                ('linkedin', models.CharField(max_length=500)),
            ],
        ),
    ]
