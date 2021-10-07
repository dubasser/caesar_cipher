alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзиёклмнопрстуфхцчшщъыьэюя'


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


def decrypt():
    temp_phrase = ''
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            temp_phrase += ' '
            continue
        if phrase[i] in alphabet_eng:
            temp_alphabet = alphabet_eng
        else:
            temp_alphabet = alphabet_ru
        if temp_alphabet.find(phrase[i]) == 0:
            temp_phrase += (temp_alphabet[len(temp_alphabet) - 1])
        else:
            temp_phrase += (temp_alphabet[temp_alphabet.find(phrase[i]) - 1])
    print(temp_phrase)
    return 0


def crypt():
    temp_phrase = ''
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            temp_phrase += ' '
            continue
        if phrase[i] in alphabet_eng:
            temp_alphabet = alphabet_eng
        else:
            temp_alphabet = alphabet_ru
        if temp_alphabet.find(phrase[i]) == len(temp_alphabet) - 1:
            temp_phrase += (temp_alphabet[0])
        else:
            temp_phrase += (temp_alphabet[temp_alphabet.find(phrase[i]) + 1])
    print(temp_phrase)
    return 0


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

