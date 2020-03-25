import telebot
import psycopg2

bot = telebot.TeleBot("953251164:AAGjwA1E-Eq7wki3oqXCSfidsp-PYun4Oy0")

user_data ={}

con = psycopg2.connect(
    host = "localhost",
    database = "restaurants",
    user = "postgres",
    password = "2825767Yer",
    port = "5432"
)

# cur = con.cursor()
# cur.execute("select restourant_name from restourants")
# rows = cur.fetchall() 


class User:
    def __init__(self, restourant_name):
        self.restourant_name = restourant_name

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
        msg = bot.send_message(message.chat.id,"Я бот поисковик какой ресторан вы ищите?")
        bot.register_next_step_handler(msg,process_search_step)

def process_search_step(message):
    try:
        user_id =  message.from_user.id
        user_data[user_id] = User(message.text)
        msg = message.text
        sql = "select * from restaurants_almaty where restaurant_name = '"+msg+"'"
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall() 
        if len(rows) == 0:
            bot.reply_to(message, "У нас нету такого ресторана")
        for j in rows:
            if j[0] in msg:
                bot.send_message(message.chat.id,str('Имя ресторана: ')+j[0])
                bot.send_message(message.chat.id,str('Адрес: ')+j[1])
                bot.send_message(message.chat.id,str('Кухни: ')+j[3])
                bot.send_message(message.chat.id,str('Контакты: ')+j[2])
                bot.send_message(message.chat.id,str('Средняя цена: ')+j[4])
                bot.send_message(message.chat.id,str('Дополнительные услуги: ')+j[5])
                break
                
    except Exception as e:
        bot.reply_to(message, "Вы ввели что-то некоректно повторите попытку")





bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()
if __name__ == '__main__':
    bot.polling(none_stop=True)
cur.close()
con.close()