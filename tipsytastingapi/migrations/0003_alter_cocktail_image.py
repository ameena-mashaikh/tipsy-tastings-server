# Generated by Django 4.1.3 on 2022-12-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipsytastingapi', '0002_alter_cocktail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='image',
            field=models.CharField(max_length=513),
        ),
    ]