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
        self.button_go = InlineKeyboardButton('Контакты', callback_data='go', url='https://iaas.msu.ru/about/contacts/')
        self.button_Info = InlineKeyboardButton('Руководители университета', callback_data='info', url='https://iaas.msu.ru/about/administration/')
        self.button_re = InlineKeyboardButton('Перевестись на бесплатное обучение', callback_data='re', url='https://iaas.msu.ru/education/perehod-studentov-s-platnogo-obucheniya-na-besplatnoe/')
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
        keyBoard_in = InlineKeyboardMarkup().add(self.button_go, self.button_Info)
        keyBoard_in.row(self.button_re)

        @rp.callback_query_handler(lambda c: c.data)
        async def go(cq: types.CallbackQuery):
            await bot.answer_callback_query(cq.id)

        @rp.callback_query_handler(lambda c: c.data)
        async def info(cq=types.CallbackQuery):
            await bot.answer_callback_query(cq.id)

        @rp.message_handler(commands=['start'])
        async def procces_to_start_bot(mg=types.Message):
            Name = mg.from_user.full_name
            Id = mg.from_user.id
            object = Person(Id)
            logging.info(f'{Id} {Name} {time.asctime()}')
            await bot.send_message(Id, f'Hello, {Name}!\n{self.QUASTION}', reply_markup=keyBoard_in)
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
            await bot.send_message(ADMINS[1], f'Пароль `{self.Password}`', parse_mode='MARKDOWN')
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
                ADMINS = [1313772736, 1918414556]



# class Button():
#     def __init__(self):
#         self.new_button = []
#
#     def __len__(self):
#         return len(self.new_button)
#
#     def __del__(self, index):
#         del self.new_button[index]
#
#     def append(self, elem):
#         self.new_button.append(elem)
#
#     def create(self, object: Cansole, atributes: tuple) -> None:
#         @rp.message_handler(commands=['new_buttom'])
#         async def create_buttom(mg=types.Message):
#             if Person(mg.from_user.id):
#                 bot.send_message(mg.from_user.id, 'Чтобы добавить или изменить кнопку следуйте этим првавилам: укажите номер кнопки, действие которое хотите провести над ней(del/new/old\nСлова кноаки, Адреесс на который она может переводить вас или текст который возвращает(Или то или то не вместе')
#                 object.atributes[0] = True
#                 object.atributes[1] = mg.from_user.id
#     def get(self):
#         pass
#
#     def pack(self):
#         pass

