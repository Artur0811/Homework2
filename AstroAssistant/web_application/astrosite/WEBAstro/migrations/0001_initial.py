# Generated by Django 3.2.19 on 2023-06-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_name', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=50)),
                ('star_type', models.CharField(max_length=10)),
                ('other_names', models.CharField(max_length=500)),
                ('magnitude', models.CharField(max_length=30)),
                ('eclipse', models.CharField(max_length=30)),
                ('period', models.CharField(default='', max_length=30)),
                ('epoch', models.CharField(default='', max_length=30)),
                ('light_curve', models.ImageField(upload_to='curve/%Y/%m/%d/')),
                ('area_photo', models.ImageField(upload_to='area/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now=True)),
                ('registered', models.BooleanField(default=False)),
            ],
        ),
    ]