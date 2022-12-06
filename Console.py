from aiogram import types
from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup
import logging, time
from Person import Person, Password
from constants import *
from RegEx import *
import sys, asyncio

# Консоль со всеми действиями
class Cansole():
    def __init__(self): # Конструктор
        self.user = InlineKeyboardButton("Для поступающих", callback_data='user')
        self.student = InlineKeyboardButton('Для студентов', callback_data='students')
        self.button_magistr = InlineKeyboardButton('Для магистратуры', callback_data="magistr")
        self.button_contact = InlineKeyboardButton('Контакты', callback_data='go')
        self.button_admins = InlineKeyboardButton('Дни открытых дверей на 2023 год', callback_data="info")
        self.button_about_free_studies = InlineKeyboardButton("Как перевестись на бесплатное обучение?", callback_data="return")
        self.button_adress = InlineKeyboardButton("Адрес", callback_data='map', url="https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%9C%D0%BE%D1%85%D0%BE%D0%B2%D0%B0%D1%8F,+11,+%D1%81%D1%82%D1%80.+1,+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,+125009/@55.7553848,37.6095687,17z/data=!3m1!4b1!4m5!3m4!1s0x46b54a503d4131f9:0xb89653ca2757f711!8m2!3d55.7553848!4d37.6117574?hl=ru")
        self.button_more_info = InlineKeyboardButton("Больше информации", callback_data="new", url="https://iaas.msu.ru/abiturientam/abiturientam-opendoors/")

        self.flag = False
        self.security = False
        self.security_id = None
        self.Password = None
        self.add_admin_flag = None
        self.set_flag = None
        self.set_id = None
        self.QUASTION = QUASTION
        self.MAIN_QUASTION = MAIN_QUASTION
        self.GO_title = 'Hi'
        self.remove_flag = False


    def start(self) -> None:#Команда старт в теллеграме
        main_key = InlineKeyboardMarkup().add(self.user, self.student, self.button_magistr)
        keyBoard_user = InlineKeyboardMarkup().add(self.button_contact, self.button_admins)
        keyBoard_students = InlineKeyboardMarkup().add(self.button_about_free_studies)
        keys = InlineKeyboardMarkup(row_width=2).add(self.button_adress)
        key_in = InlineKeyboardMarkup().add(self.button_more_info)

        @rp.callback_query_handler(lambda c: (c.data == 'magistr'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)
            await bot.send_message(cq.from_user.id, "Информация для магистратуры")

        @rp.callback_query_handler(lambda c: (c.data == 'user'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)
            await bot.send_message(cq.from_user.id, "Информация для поступающих", reply_markup=keyBoard_user)

        @rp.callback_query_handler(lambda c: (c.data == 'students'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)
            await bot.send_message(cq.from_user.id, "Информация для учащихся", reply_markup=keyBoard_students)

        @rp.callback_query_handler(lambda c: (c.data == 'return'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)
            await bot.send_message(cq.from_user.id, "Перевод с любого факультета обсуждается с администрацией. Но обязательно нужно узнать есть ли свободные бесплатные места (это можно узнать здесь 👉🏼 http://edu.msu.ru/plata/). За помощью можете обращаться в институтский совет студентов(Просто напишите в чат боте вопрос) или в профсоюз по номеру телефона `+7 (495) 629-43-49`. Студентам 1 курса нельзя перевестись на бесплатное обучение:(.", parse_mode="MARKDOWN")

        @rp.callback_query_handler(lambda c: (c.data == 'new'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)

        @rp.callback_query_handler(lambda c: (c.data == 'info'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)
            await bot.send_message(cq.from_user.id, "Дни открытых дверей:\n📆18 мая 2023 год 19:00\n📆20 марта 2023 13:00 - 15:00\n📆20 февраля 13:00 - 15:00(для иностранных поступающих)", reply_markup=key_in)

        @rp.callback_query_handler(lambda c: (c.data == 'map'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)

        @rp.callback_query_handler(lambda c: (c.data == 'go'))
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)
            await bot.send_message(cq.from_user.id, "☎Телефон: `+7 (495) 629-43-49`\n📩Почта: `office@iaas.msu.ru`\n📫Адрес: 125009, г. Москва, ул. Моховая, д. 11, стр. 1(Ссылка на google maps👇)", reply_markup=keys, parse_mode="MARKDOWN")


        @rp.message_handler(commands=['start'])
        async def procces_to_start_bot(mg=types.Message):
            Name = mg.from_user.full_name
            Id = mg.from_user.id
            object = Person(Id)
            logging.info(f'{Id} {Name} {time.asctime()}')
            await bot.send_message(Id, f'Hello, {Name}!\n{self.QUASTION}', reply_markup=main_key)
            if object():
                await bot.send_message(Id, f'{self.MAIN_QUASTION}')
            return None

    def send(self)->None:#Обычное перехватывание сообщение
        @rp.message_handler(content_types='text')
        async def proccess_to_send_message(mg=types.Message):
            object = Person(mg.from_user.id)
            if object():
                if self.set_flag:
                    object = Set()
                    if Check_result(object(mg.text)):
                        await bot.send_message(mg.from_user.id, 'Вы могли допустить ошибку в сообщение.')
                        return None

                    start_title, end_title = object(mg.text)
                    if start_title == '1':
                        self.QUASTION = end_title
                    elif start_title == '2':
                        self.MAIN_QUASTION = end_title
                    elif start_title == '3':
                        self.GO_title = end_title
                    self.set_falg = False
                    return None

                elif self.flag:
                    object = Text()
                    if Check_result(object(mg.text)):
                        await bot.send_message(mg.from_user.id, 'Вы могли допустить ошибку в сообщение.')
                        return None
                    id, text = object(mg.text)
                    try:
                        await bot.send_message(id, text)
                    except:
                        await bot.send_message(mg.from_user.id, 'id должно состоять из 10 чисел')

                    self.flag = False
                    return None

                elif self.security:
                    if mg.text == self.Password:
                        await bot.send_message(self.security_id, f'`{TOKEN}`', parse_mode='MARKDOWN')
                    self.security = False
                    self.security_id = None
                    return None

                elif self.remove_flag:
                    Id = mg.text
                    try:
                        Index = ADMINS.index(int(Id))
                        del ADMINS[Index]
                        await bot.send_message(mg.from_user.id, 'Админ был удалён.')
                    except:
                        await bot.send_message('Наверное вы указали не правильное Id')

            if self.add_admin_flag and mg.from_user.id == self.security_id:
                if mg.text == self.Password:
                    ADMINS.append(self.security_id)
                    await bot.send_message(self.security_id, 'Теперь вы админ')
                self.add_admin_flag = False
                self.security_id = None
                self.Password = None
                return None

            Name = mg.from_user.full_name
            Id = mg.from_user.id
            object = Person(Id)
            if object():
                return None
            await bot.send_message(ADMINS[1], f'Hello, @Asomersby. You have one more message from {Name}, id adress is `{Id}`:\n{mg.text}', parse_mode='MARKDOWN')
            await bot.send_message(ADMINS[1], 'To resend an answear print command, id and message')
            return None

    def resend(self)->None:#Переправка сообщений(Только для администраторов)
        @rp.message_handler(commands=['resend'], content_types='text')
        async def procces_to_resend_message(mg=types.Message):
            self.flag = True
            await mg.reply('Что бы ответить: 1. Используйте формат: Id - Message(нужно обязательно ставить пробелы между всеми словами), 2. Отвечать можно полсе использования команды /resend')

    def get(self) -> None:#Получение токена из телеграмма
        @rp.message_handler(commands=['get'], content_types='text')
        async def procces_to_get_Token(mg=types.Message):
            object = Password()
            self.Password = object()
            self.security = True
            self.security_id = mg.from_user.id
            await bot.send_message(ADMINS[1], f'Пароль `{self.Password}`', parse_mode='MARKDOWN ')
            await bot.send_message(self.security_id, 'Что бы получить токен введите пороль, посланный администратору.')


    def add(self):
        @rp.message_handler(commands=['add'])
        async def procces_to_add_admins(mg=types.Message):
            if self.security_id != None:
                await asyncio.sleep(10)
            await bot.send_message(mg.from_user.id, 'Что бы добавить нового админа, нужно ввести пороль который прислали главному админу')
            self.add_admin_flag = True
            object = Password()
            self.security_id = mg.from_user.id
            self.Password = object()
            await bot.send_message(ADMINS[1], f'`{self.Password}`', parse_mode='MARKDOWN')

    def set(self):
        @rp.message_handler(commands=['set'])
        async def procces_to_set(mg=types.Message):
            object = Person(mg.from_user.id)
            if not object():
                return None
            elif object():
                await bot.send_message(mg.from_user.id, f'Чтобы изменит реплики бота следуйте этому шаблону: номер реплики - Новая репоика\n Список реплик перечислен ниже:\n\t 1 - {QUASTION}\n\t 2 - {MAIN_QUASTION}\n\t 3 - {self.GO_title} \nPs Чтобы поменять две или больше реплик нужно вызывать команду /set')
                self.set_flag = True
    def riot(self):
        @rp.message_handler(commands=['riot'])
        def exit_procces(mg=types.Message):
            object = Person(mg.from_user.id)
            if object():
                sys.exit('Error: Call to exit: Tellegram call')
            else:
                return None
    def destroy(self):
        @rp.message_handler(commands=['remove'])
        async def remove_procces(mg=types.Message):
            if Person(mg.from_user.id):
                self.remove_flag = True
                await bot.send_message(mg.from_user.id, 'Просто запишите id')
    def restart(self):
        @rp.message_handler(commands=['restart'])
        async def restart_procces(mg=types.Message):
            global ADMINS
            if Person(mg.from_user.id):
                self.flag = False
                self.security = False
                self.security_id = None
                self.Password = None
                self.add_admin_flag = None
                self.set_flag = None
                self.QUASTION = QUASTION
                self.MAIN_QUASTION = MAIN_QUASTION
                self.GO_title = 'Hi'
                self.remove_flag = False
                ADMINS = ["Your id"]



