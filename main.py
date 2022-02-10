import telebot
import time
import random
l = list(range(1, 250))
random.shuffle(l)
bot = telebot.TeleBot('5169529686:AAHyDn-WzkVbhAXG2c-eDRMoPXWSB3dV7wE')
CHANNEL_NAME = '@forUwichLove'
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
for i in l:
    mess = jokes[i]
    print(mess)
    bot.send_message(CHANNEL_NAME, mess)
    time_sl = random.randrange(1800,3600,60)
    print(time_sl)
    time.sleep(time_sl)
bot.send_message(CHANNEL_NAME, " Красивые словечки кончились. Димка скоро их добавит.")
