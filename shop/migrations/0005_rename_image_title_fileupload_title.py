# Generated by Django 5.1.4 on 2024-12-10 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_fileupload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='image_title',
            new_name='title',
        ),
    ]
