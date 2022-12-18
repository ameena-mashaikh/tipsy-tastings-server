#!/bin/bash
#./seed_database.sh


rm db.sqlite3
rm -rf ./tipsytastingapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations tipsytastingapi
python3 manage.py migrate tipsytastingapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata mixologists
python3 manage.py loaddata liquors
python3 manage.py loaddata liqueurs
python3 manage.py loaddata staple_ingredients
python3 manage.py loaddata category
python3 manage.py loaddata cocktails
python3 manage.py loaddata cocktail_posts
python3 manage.py loaddata cocktail_liquors
python3 manage.py loaddata cocktail_liqueurs
python3 manage.py loaddata cocktail_staple_ingredients


