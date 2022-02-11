import telebot
from colorama import init, Fore
from prettytable import PrettyTable

init()

token = '' #<----put your bot token here

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    ptable = PrettyTable()
    ptable.field_names = ["ID", "USER NAME", "FIRST NAME", "LAST NAME"]
    ptable.add_rows(
    [
        [f"{message.chat.id}", f'{message.from_user.username}', f'{message.from_user.first_name}', f'{message.from_user.last_name}'],
    ]
)
    #s = f'id: {message.chat.id}\nusername: {message.from_user.username}\nfirst name: {message.from_user.first_name}\nlast name: {message.from_user.last_name}'
    print(Fore.GREEN + f'{ptable}')


@bot.message_handler(content_types=['text'])
def text(message):
    ptable2 = PrettyTable()
    if message.from_user.username == None:
        name = message.from_user.first_name
    else:
        name = message.from_user.username
    ptable2.field_names = ['USERNAME', 'MESSAGE']
    ptable2.add_rows(
    [
        [f'{name}', f'{message.text}'],
    ]
    )
    print(Fore.GREEN + f'{ptable2}')


bot.polling(none_stop=True, interval=0)
