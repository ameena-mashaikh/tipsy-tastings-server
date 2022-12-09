#!/bin/bash
#./seed_database.sh


rm db.sqlite3
rm -rf ./tipsytastingapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations tipsytastingapi
python3 manage.py migrate tipsytastingapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata mixologist
python3 manage.py loaddata liquor
python3 manage.py loaddata liqueur
python3 manage.py loaddata staple_ingredient
python3 manage.py loaddata category
python3 manage.py loaddata cocktail
python3 manage.py loaddata cocktail_post
python3 manage.py loaddata cocktail_liquor
python3 manage.py loaddata cocktail_liqueur
python3 manage.py loaddata cocktail_staple_ingredients


