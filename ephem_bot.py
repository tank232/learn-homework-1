"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)



def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
def galaxy_planet(bot, update):
    user_text = update.message.text.split()
    planet=user_text[1]
    now = datetime.datetime.now()

    if planet=='mars':
        planet_info = ephem.Mars(now)
    elif planet=='mercury':
        planet_info = ephem.Mercury(now)
    elif planet=='jupiter':
        planet_info = ephem.Jupiter(now)
    elif planet=='saturn':
        planet_info = ephem.Saturn(now)
    update.message.reply_text(ephem.constellation(planet_info))



def main():
    mybot = Updater(settings.API_KEY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", galaxy_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
