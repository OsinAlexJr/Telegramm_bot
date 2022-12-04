# Make Telegramm bot
#By Osin Alexey, @alexey_addams
from constants import rp
from aiogram import executor
from Console import Cansole


object = Cansole()
object.restart()
object.destroy()
object.set()
object.start()
object.add()
object.get()
object.resend()
object.send()


if __name__ == '__main__':
    executor.start_polling(rp)

#BETA version

