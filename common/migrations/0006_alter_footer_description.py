# Generated by Django 5.1.7 on 2025-03-13 03:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_footer_description_alter_footer_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
