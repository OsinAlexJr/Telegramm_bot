import TranspositionCipher, random
from constants import *
#Персонализация

class Person():

    def __init__(self, id, phone_number=None):
        self.id = id
        self.phone_number = phone_number

    def __call__(self) -> bool:
        object = Admin(self.id)
        return bool(object)


class Admin():
    def __init__(self, id):
        self.id = id

    def __bool__(self):
        for person in range(len(ADMINS)):
            if int(self.id) == int(ADMINS[person]):
                return True

        return False


class Password:
    def __init__(self):
        self.list = ['I', 't', 'i', 's', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', '!', '1', '9']
        self.password = (TranspositionCipher.EncryptMessage(random.randint(2, 11), ''.join(self.list)))

    def __call__(self):
        return self.password

    def __int__(self):
        return len(self.list)

