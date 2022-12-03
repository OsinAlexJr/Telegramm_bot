# Программа для перестановочного шифра
# name is trasparation exncrypt/ (Bsd lincensed)
# Первая функция, которая при имортирование не будет вызываться
import os, re, pyperclip
def main():
    # Ваша информация
    MyMessage = input('Your text or name of file: ')
    if os.path.exists(MyMessage):
        file = open(MyMessage, 'r')
        fileText = file.read()
        file.close()
        MyMessage = fileText
    MyKey = eval(input('Your secret nomber: '))
    MyMode = input('You will encrypt or decrypt: ')
    control = re.findall(r'^\w?', MyMode)
    print(control)
    if control == ['E'] or ['e']:
        text = EncryptMessage(MyKey, MyMessage)
    elif control == ['D'] or ['d']:
        text = DecryptMessage(MyKey, MyMessage)
    pyperclip.copy(text)
    print('Your text us %s and it has been copied to your clip board' % (text))
    print('Your Key is #%s' % (MyKey))

def EncryptMessage  (key, message):
    ciphertext = [''] * key
    for column in range(key):
        TransIndex = column

        while TransIndex < len(message):
            ciphertext[column] += message[TransIndex]

            TransIndex += key

    answear = ''.join(ciphertext)
    return answear

def DecryptMessage(key, message):
    NumOfColumns = int(math.ceil(len(message)/ float(key)))
    NumOfRow = key
    DelNum = (NumOfColumns* NumOfRow) - len(message)
    plaintext = [''] * NumOfColumns
    column = 0
    row = 0
    
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == NumOfColumns) or (column == NumOfColumns - 1 and row >= NumOfRow - DelNum):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()

SECURETY_MODE = ['TranspositionCipher', 'EncryptMessage', 'DecryptMessage']



