# Generated by Django 4.1.6 on 2023-02-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tguser',
            old_name='varification_code',
            new_name='verification_code',
        ),
    ]