# Generated by Django 5.1.4 on 2024-12-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_image_title_fileupload_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]