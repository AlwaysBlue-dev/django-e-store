# Generated by Django 4.1.4 on 2023-01-18 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_chead0_blogpost_chead1_blogpost_chead2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='product_name',
            new_name='tilte',
        ),
    ]
