# Generated by Django 4.1.6 on 2023-02-07 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_rename_title_goalcomment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='data_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='data_update',
            new_name='update',
        ),
        migrations.RenameField(
            model_name='goalcategory',
            old_name='data_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='goalcategory',
            old_name='data_update',
            new_name='update',
        ),
        migrations.RenameField(
            model_name='goalcomment',
            old_name='data_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='goalcomment',
            old_name='data_update',
            new_name='update',
        ),
    ]