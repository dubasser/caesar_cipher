alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзиёклмнопрстуфхцчшщъыьэюя'

#Функция ввода фразы
def phrase_input():
    while True:
        wo_spaces_phrase = ''
        inputed_phrase = (input('Введите фразу(только из букв):'))
        for i in range(len(inputed_phrase)):
            if inputed_phrase[i] == ' ':
                continue
            else:
                wo_spaces_phrase += inputed_phrase[i]
        if wo_spaces_phrase.isalpha():
            break
        else:
            print('Введеная вами фраза содержит посторонние символы. Повторите попытку.')
    return inputed_phrase

#Дешиврование
def decrypt():
    temp_phrase = ''
    step = int(input('Введите шаг шифрования/дешифровровния:'))
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            temp_phrase += ' '
            continue
        if phrase[i] in alphabet_eng:
            temp_alphabet = alphabet_eng
        else:
            temp_alphabet = alphabet_ru
        # Получившееся слово
        temp_phrase += (temp_alphabet[(temp_alphabet.find(phrase[i]) - step) % len(temp_alphabet)])
    print(temp_phrase)
    return 0

#Шиврование
def crypt():
    temp_phrase = ''
    step = int(input('Введите шаг шифрования/дешифровровния:'))
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            temp_phrase += ' '
            continue
        if phrase[i] in alphabet_eng:
            temp_alphabet = alphabet_eng
        else:
            temp_alphabet = alphabet_ru
        # Получившееся слово
        temp_phrase += (temp_alphabet[(temp_alphabet.find(phrase[i]) + step) % len(temp_alphabet)])
    print(temp_phrase)
    return 0

#Основной цикл программы
while True:
    phrase = phrase_input()
    temp = int(input('Чтобы зашифровать фразу введите 0, чтобы расшифровать введите 1. Для выхода введите 3:'))
    if temp == 0:
        crypt()
    elif temp == 1:
        decrypt()
    elif temp == 3:
        raise SystemExit
    else:
        print('Неверный формат ввода')
