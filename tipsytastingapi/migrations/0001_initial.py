# Generated by Django 4.1.3 on 2022-12-08 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('recipe', models.CharField(max_length=800)),
                ('image', models.CharField(max_length=513)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cocktail_category', to='tipsytastingapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='CocktailPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('caption', models.CharField(max_length=200)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_cocktail', to='tipsytastingapi.cocktail')),
            ],
        ),
        migrations.CreateModel(
            name='Liqueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Liquor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='StapleIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Mixologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=513)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocktail_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipsytastingapi.cocktailpost')),
                ('mixologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipsytastingapi.mixologist')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('cocktail_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipsytastingapi.cocktailpost')),
                ('mixologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipsytastingapi.mixologist')),
            ],
        ),
        migrations.CreateModel(
            name='CocktailStapleIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=None, null=True)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staples_for_cocktail', to='tipsytastingapi.cocktail')),
                ('staple_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staple_needed_for_cocktail', to='tipsytastingapi.stapleingredient')),
            ],
        ),
        migrations.AddField(
            model_name='cocktailpost',
            name='mixologist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mixologist_post', to='tipsytastingapi.mixologist'),
        ),
        migrations.CreateModel(
            name='CocktailLiquor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=None)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liquor_for_cocktail', to='tipsytastingapi.cocktail')),
                ('liquor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liquor_needed_for_cocktail', to='tipsytastingapi.liquor')),
            ],
        ),
        migrations.CreateModel(
            name='CocktailLiqueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=None, null=True)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liqueur_for_cocktail', to='tipsytastingapi.cocktail')),
                ('liqueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liqueur_needed_for_cocktail', to='tipsytastingapi.liqueur')),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='created_by_mixologist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cocktail_mixologist', to='tipsytastingapi.mixologist'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='liqueurs',
            field=models.ManyToManyField(through='tipsytastingapi.CocktailLiqueur', to='tipsytastingapi.liqueur'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='liquors',
            field=models.ManyToManyField(through='tipsytastingapi.CocktailLiquor', to='tipsytastingapi.liquor'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='staple_ingredients',
            field=models.ManyToManyField(through='tipsytastingapi.CocktailStapleIngredient', to='tipsytastingapi.stapleingredient'),
        ),
    ]
