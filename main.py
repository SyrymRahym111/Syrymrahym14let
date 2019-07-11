import telebot
from telebot import types
import config
import bs4
from urllib.request import urlopen
import re
import flask


bot = telebot.TeleBot(config.token)
server = flask.Flask(_name_)

link = 'http://filmix.cc'
genre = ''
genre1 = ''

@bot.message_handler(commands=['start'])
def start(message) :
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Фильмы', 'Сериалы']])
    msg = bot.send_message(message.chat.id, 'Здраствуйте!Я "Films & TV Series bot" помогу найти фильмы или сериалы которые указаны на кнопках.Что  хотите посмотреть? Фильмы или Сериалы?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Фильмы' :
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Приключение', 'Драма', 'Ужасы', 'Фантастика', 'Боевик', 'Триллер']])
        msg = bot.send_message(message.chat.id, 'Выберите какой жанр фильма вы хотите посмотреть?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, saw)
    if message.text == 'Сериалы' :
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Биография', 'Семейный', 'Комедии', 'Игра', 'Детектив', 'Аниме']])
        msg = bot.send_message(message.chat.id, 'Выберите какой жанр сериала вы хотите посмотреть?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, see)
def saw(message):
    global genre
    if message.text == 'Приключение':
        genre = 'priklucheniya'
        msg = bot.send_message(message.chat.id, 'Вперед в приключение,подождите 1 минуточку мы подбираем фильмы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(message)
    elif message.text == 'Драма' :
        genre = 'dramy'
        msg = bot.send_message(message.chat.id, 'Неееееет джони не умирай :3 ,подождите 1 минуточку мы подбираем фильмы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(message)
    elif message.text == 'Ужасы' :
        genre = 'uzhasy'
        msg = bot.send_message(message.chat.id, 'Любите "Ужасы"?,подождите 1 минуточку мы подбираем фильмы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(message)
    elif message.text == 'Фантастика' :
        genre = 'fantastika'
        msg = bot.send_message(message.chat.id, 'А что если все фантастические герои или монстры ожили ?,подождите 1 минуточку мы подбираем фильмы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(message)
    elif message.text == 'Боевик' :
        genre = 'boeviki'
        msg = bot.send_message(message.chat.id, 'Headshot :),подождите 1 минуточку мы подбираем фильмы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(message)
    elif message.text == 'Триллер' :
        genre = 'trillery'
        msg = bot.send_message(message.chat.id, 'Хехехехехе,подождите 1 минуточку мы подбираем фильмы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(message)
def see(message) :
    global genre
    if message.text == 'Биография':
        genre1 = 'biografia'
        msg = bot.send_message(message.chat.id, 'Надеюсь вы узнаете больше чем в школе :3 ,подождите 1 минуточку мы подбираем сериалы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(mess)
    elif message.text == 'Семейный' :
        genre1 = 'semejnyj'
        msg = bot.send_message(message.chat.id, 'Желаю твоей маме, папе, дедушке, бабушке , братику, сестренке приятного просмотора,подождите 1 минуточку мы подбираем сериалы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(mess)
    elif message.text == 'Комедии' :
        genre1 = 'komedii'
        msg = bot.send_message(message.chat.id, '"Хахахахаха"Даю слово будет смешно ;) ,подождите 1 минуточку мы подбираем сериалы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(mess)
    elif message.text == 'Игра' :
        genre1 = 'game'
        msg = bot.send_message(message.chat.id, 'Любите игры?,подождите 1 минуточку мы подбираем сериалы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(mess)
    elif message.text == 'Детектив' :
        genre1 = 'detektiv'
        msg = bot.send_message(message.chat.id, 'Думаю вам понравится что мы вам предложем ,подождите 1 минуточку мы подбираем сериалы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(mess)
    elif message.text == 'Аниме' :
        genre1 = 'anime'
        msg = bot.send_message(message.chat.id, 'Интересно,интересно,хорошо,подождите 1 минуточку мы подбираем сериалы...')
        bot.register_next_step_handler(msg, parsing)
        parsing(mess)
    
def parsing(message) :
    global link
    global genre
    links = link+genre
    html_page = urlopen(links)
    soup = bs4.BautifulSoup(html_page, 'html.parser')
    for link in soup.findAll('a'):
        href = link.get('href')
        if href.endswith('.html') :
            bot.send_message(message.chat.id, href)
def parsing(mess):
    global link
    global genre1
    links = link+genre1
    html_page = urlopen(links)
    soup = bs4.BeautifulSoup(html_page, 'html.parser')
    for link in soup.findAll('a'):
        href = link.get('href')
        if href.endswith('.html') :
            bot.send_message(message.chat.id, href)
        
        
    
       
            




    
    
    
    @server.route('/' + config.token, =['POST'])
    def get_message() :
         bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8))])
         return "!", 200

    @server.route('/', methods=["GET"])
    def index():
         print("Hello webhook!")
         bot.remove_webhook()
         bot.set_webhook(url=f"https://{config.APP_NAME}.herokuapp.com/{config.token}")
         return "hello from heroku!", 200
         
    print(f"https://{config.APP_NAME}.herokuapp.com/{config.token})
    print(f"PORT: {int(os.environ.get('PORT', 5000))}")
    if __name__ == "__main__":
    bot.polling(none_stop = True)
    print("started")
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
