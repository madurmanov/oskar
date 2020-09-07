import os
from boto.s3.connection import S3Connection

telegram_api_key = os.environ['TELEGRAM_API_KEY']
bot_name = os.environ['BOT_NAME']
kinochat_id = -1001323316776
members_list = [
    {
        'username': '@molotoko',
        'gender': 'female'
    },
    {
        'username': '@HKEY47',
        'gender': 'male'
    },
    {
        'username': '@mikmall',
        'gender': 'male'
    },
    {
        'username': '@madurmanov',
        'gender': 'male'
    },
    {
        'username': '@fyvdlo',
        'gender': 'male'
    },
    {
        'username': '@wilddeer',
        'gender': 'male'
    },
    {
        'username': '@Henpukuhime',
        'gender': 'female'
    },
    {
        'username': '@anechka_persik',
        'gender': 'female'
    },
    {
        'username': '@sleepercat0_0',
        'gender': 'female'
    },
    {
        'username': '@Milli_M',
        'gender': 'female'
    },
    {
        'username': '@Dart_gedark',
        'gender': 'male'
    },
    {
        'username': '@nogpyra',
        'gender': 'female'
    },
    {
        'username': '@tsynali',
        'gender': 'female'
    },
    {
        'username': '@kokos_89',
        'gender': 'male'
    },
    {
        'username': '@beforescriptum',
        'gender': 'female'
    },
    {
        'username': '@MoshWayne',
        'gender': 'male'
    }

]
stickers_list = {
    'droed': 'CAACAgIAAxkBAAO1Xrs0GAK_ts-_2AG5lhTO2VwRTS4AAl0BAAJEyQkHfIbn433Oi2gZBA',
    'droed_work': 'CAACAgIAAxkBAAOvXrszrgvwIgKSJj105YntGMYTL7cAAl4BAAJEyQkHQhFYn9ziwn4ZBA'
}

s3 = S3Connection(telegram_api_key, bot_name)
