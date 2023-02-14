# Generated by Django 4.1.3 on 2023-01-09 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipsytastingapi', '0003_alter_cocktail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syrup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.AddField(
            model_name='cocktailpost',
            name='liked_users',
            field=models.ManyToManyField(through='tipsytastingapi.Likes', to='tipsytastingapi.mixologist'),
        ),
        migrations.CreateModel(
            name='CocktailSyrup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syrup_for_cocktail', to='tipsytastingapi.cocktail')),
                ('liqueur', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='syrup_needed_for_cocktail', to='tipsytastingapi.syrup')),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='syrups',
            field=models.ManyToManyField(through='tipsytastingapi.CocktailSyrup', to='tipsytastingapi.syrup'),
        ),
    ]