# Costants for telegramm bot
# Api

from aiogram import Bot, Dispatcher
# Token

TOKEN = 'Ваш Token'
# Replicas

QUASTION = 'Welcome to HelpBot.\nЧто бы спросить вопрос у сотрудников Института просто отправьте сообщение боту.'
MAIN_QUASTION = 'Привет, добро пожаловать в настройки бота Help bot by @Asomersby and @alexey_addams:\n\t\t1.Получить Токен: /get, 2.Новые реплики: /set, 3.Добавить админа: /add\n\t\t4. Убрать адмига: /remove, 5.Переслать сообщение: /resend\n\t\t6.Перезагрузить бота: /restart'
# ID's

ADMINS = ['Ваш Id']

#Bot's
bot = Bot(token=TOKEN) # To use in foreign server better use some proxy instead VPN (I'm use pythonanywhere)
rp = Dispatcher(bot=bot)
