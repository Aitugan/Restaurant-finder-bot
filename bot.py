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
        msg = bot.send_message(message.chat.id,"Hi! I'm a restaurant finder-bot! What restaurant would you want to find recommendation on?")
        bot.register_next_step_handler(msg,process_search_step)




bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
cur.close()
con.close()