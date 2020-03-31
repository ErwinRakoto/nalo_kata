#!/usr/bin/env bash
#set -e pipefail

python3 -m pip3 install virtualenv
python3 -m virtualenv venv

if [[ "$OSTYPE" == "msys" ]]; then
   source venv/Scripts/activate
else
   source venv/bin/activate
fi

pip install -U pip
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate


echo -e "\n Just run : python manage.py runserver \n and you get it !"
