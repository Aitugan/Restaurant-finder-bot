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


class User:
    def __init__(self, restourant_name):
        self.restourant_name = restourant_name

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
        msg = bot.send_message(message.chat.id,"Hi! I'm a restaurant finder-bot! What restaurant would you want to find recommendation on?")
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
            bot.reply_to(message, "Sorry, but we do not have that restaurant...")
        for j in rows:
            if j[0] in msg:
                bot.send_message(message.chat.id,str('Restaurant name: ')+j[0])
                bot.send_message(message.chat.id,str('Address: ')+j[1])
                bot.send_message(message.chat.id,str('Cuisines: ')+j[3])
                bot.send_message(message.chat.id,str('Contacts: ')+j[2])
                bot.send_message(message.chat.id,str('Average price: ')+j[4])
                bot.send_message(message.chat.id,str('More: ')+j[5])
                break
                
    except Exception as e:
        bot.reply_to(message, "Oops, you entered something incorrect..")

bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
cur.close()
con.close()