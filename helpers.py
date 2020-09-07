import random
import requests
import lxml.html as html
from config import kinochat_id


def get_random_actor(gender):
    link = 'https://www.imdb.com/search/name/?groups=oscar_winner,oscar_nominee&count=100'

    if gender:
        link = f'{link}&gender={gender}'

    actors_request = requests.get(link)
    actors_tree = html.fromstring(actors_request.text)
    actors = actors_tree.find_class('lister-item')

    actor = random.choice(actors).find_class('lister-item-header')[0].find('a')
    actor_name = actor.text_content().strip()
    actor_href = actor.attrib['href']
    actor_link = f'https://www.imdb.com{actor_href}'

    actor_request = requests.get(actor_link)
    actor_tree = html.fromstring(actor_request.text)
    actor_death_info = actor_tree.xpath('//div[@id="name-death-info"]')

    return {
        'name': actor_name,
        'link': actor_link,
        'alive': False if len(actor_death_info) else True
    }


def born_today_cron():
    request_link = 'https://www.imdb.com/feature/bornondate/'
    page = requests.get(request_link)
    tree = html.fromstring(page.text)

    born_list = []
    celebrities = tree.find_class('lister-item')[:5]

    for celebrity in celebrities:
        celebrity_anchor = celebrity.find_class('lister-item-header')[0].find('a')
        celebrity_name = celebrity_anchor.text_content().strip()
        celebrity_link = celebrity_anchor.attrib['href']
        born_list.append([celebrity_name, celebrity_link])

    born_message = f'Сегодня родились знаменитости:\n'
    for celebrity in born_list:
        born_message += f'[{celebrity[0]}](https://www.imdb.com{celebrity[1]})\n'

    bot.send_message(
        kinochat_id,
        born_message,
        parse_mode='Markdown'
    )


def notifications():
    schedule.every().day.at('10:00').do(born_today_cron())
    while True:
        schedule.run_pending()
        time.sleep(1)
