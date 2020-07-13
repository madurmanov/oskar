import random
import telebot
import requests
import lxml.html as html
import unicodedata
from config import telegram_api_key

bot = telebot.TeleBot(telegram_api_key)
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
    }
]
stickers_list = {
    'droed': 'CAACAgIAAxkBAAO1Xrs0GAK_ts-_2AG5lhTO2VwRTS4AAl0BAAJEyQkHfIbn433Oi2gZBA',
    'droed_work': 'CAACAgIAAxkBAAOvXrszrgvwIgKSJj105YntGMYTL7cAAl4BAAJEyQkHQhFYn9ziwn4ZBA'
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, о киноман!')


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(
        message.chat.id,
        f'Добро пожаловать к Оскару в Киноклуб! Не считая меня, в клубе уже *{len(members_list)}* участников! '
        f'Ниже представлен список моих услуг. '
        f'Помните: судьба может сыграть с вами злую шутку!\n'
        f'/member расскажет обо всех ваших кинотайнах;\n'
        f'/film выберет за вас случайное кино;\n'
        f'/genre поможет выбрать жанр для голосований (если повезет — с эротикой);\n'
        f'/vip определит особо голосистого участника этого голосования: '
        f'может отдать 4 голоса вместо 2, максимум 2 за 1 фильм;\n'
        f'/kinoman даст одному из вас возможность сразу предложить фильм вне очереди.\n'
        f'/droed пнуть робота.',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['member'])
def member_info(message):
    get_info = 'собрать инфу из таблички'
    find_member_info = 'вытащить инфу о конкретном члене клуба'
    bot.send_message(
        message.chat.id,
        f'Ваша статистика пока недоступна. И будет недоступна еще какое-то время. Заполняйте табличку!'
    )


@bot.message_handler(commands=['film'])
def random_film(message):
    page = requests.get('https://www.kinopoisk.ru/afisha/new/city/1/')
    tree = html.fromstring(page.text)
    film_name = tree.xpath('//div[@class="randomMovie"]//a/span/u/text()')[0]
    film_name_normalized = unicodedata.normalize("NFKD", film_name)
    film_path = 'film/301/'

    all_links = list(tree.iterlinks())
    for link in all_links:
        (element, attribute, url, pos) = link
        if 'level/1/film' in url:
            film_path = url[8:]
    film_link = f'https://www.kinopoisk.ru{film_path}'

    bot.send_message(
        message.chat.id,
        f'Вам придется посмотреть фильм "{film_name_normalized}": {film_link}',
        reply_to_message_id=message.message_id
    )


@bot.message_handler(commands=['genre'])
def random_genre(message):
    genre_list = ['аниме', 'биография', 'боевик', 'вестерн', 'военный', 'детектив', 'документальный', 'драма',
                  'история', 'комедия', 'короткометражка', 'криминал', 'мелодрама', 'музыка', 'мультфильм',
                  'приключения', 'семейный', 'спорт', 'триллер', 'ужасы', 'фантастика', 'фильм-нуар', 'фэнтези']
    genre_value = random.choice(genre_list)

    erotic = ' с эротикой'
    if random.randrange(0, 100) < 2:
        genre_value = f'{genre_value}{erotic}'

    bot.send_message(
        message.chat.id,
        f'*Выбран жанр*: {genre_value}.',
        parse_mode='Markdown',
        reply_to_message_id=message.message_id
    )


@bot.message_handler(commands=['vip'])
def get_vip(message):
    random_member = random.choice(members_list)
    random_member_username = random_member['username']

    bot.send_message(
        message.chat.id,
        f'Киноман *{random_member_username}* получил статус *VIP*. Это значит, что он имеет 4 голоса вместо 2 и может '
        f'распределить их как угодно, но не более 2 голосов за 1 фильм.',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['kinoman'])
def kinoman_of_the_week(message):
    random_member = random.choice(members_list)
    random_member_username = random_member['username']

    bot.send_message(
        message.chat.id,
        f'Киноман *{random_member_username}* становится почетным *Киноманом Недели*. '
        f'Он может предложить любой фильм к просмотру вне очереди!',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['santa'])
def santa(message):
    random_member = random.choice(members_list)
    random_member_username = random_member['username']

    bot.send_message(
        message.chat.id,
        f'Киноман *{random_member_username}* становится Сантой. '
        f'Он может предложить любой фильм к просмотру вне очереди!\n'
        f'Этот фильм мы занесем в Коллективные просмотры!',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['droed'])
def go_to_work(message):
    bot.send_sticker(message.chat.id, stickers_list['droed'])
    bot.send_sticker(message.chat.id, stickers_list['droed_work'])


@bot.message_handler(commands=['date'])
def random_actor(message):
    username = f'@{message.from_user.username}'

    member_gender = None
    for member in members_list:
        if member['username'] == username:
            member_gender = member['gender']
            break

    request_link = 'https://www.imdb.com/search/name/?groups=oscar_winner,oscar_nominee&count=100'
    request_gender = None
    if member_gender == 'male':
        request_gender = 'female'
    elif member_gender == 'female':
        request_gender = 'male'

    if request_gender:
        request_link = f'{request_link}&gender={request_gender}'

    page = requests.get(request_link)
    tree = html.fromstring(page.text)

    actors = tree.find_class('lister-item')
    actor = random.choice(actors)
    actor_anchor = actor.find_class('lister-item-header')[0].find('a')
    actor_name = actor_anchor.text_content().strip()
    actor_link = actor_anchor.attrib['href']

    bot.send_message(
        message.chat.id,
        f'Ты идешь на свидание с *{actor_name}*!\n'
        f'https://www.imdb.com{actor_link}',
        parse_mode='Markdown'
    )


@bot.message_handler(content_types=['text'])
def send_text(message):
    hello_list = ['привет', 'hello', 'hi', 'приветствую', 'здравствуй', 'здравствуйте', 'хелло', 'хэлло', 'йоу',
                  'здрасьте', 'дратути', 'драсьте']
    if message.text.lower() in hello_list:
        bot.send_message(message.chat.id, 'Привет, киноман!', reply_to_message_id=message.message_id)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'I\'ll be back!', reply_to_message_id=message.message_id)
    elif 'дроед' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOvXrszrgvwIgKSJj105YntGMYTL7cAAl4BAAJEyQkHQhFYn9ziwn4ZBA')
    elif 'дроид' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOvXrszrgvwIgKSJj105YntGMYTL7cAAl4BAAJEyQkHQhFYn9ziwn4ZBA')


# @bot.message_handler(content_types=['sticker'])
# def send_sticker_id(message):
#     bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()
