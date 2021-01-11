# Generated by Django 3.1.4 on 2021-01-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsiteafs200', '0002_welcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Css',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slick', models.FileField(upload_to='css')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=50)),
                ('p', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('h5', models.CharField(max_length=50)),
                ('span', models.CharField(max_length=50)),
            ],
        ),
    ]