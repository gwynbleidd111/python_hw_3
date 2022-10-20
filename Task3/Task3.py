Задача №3___________________________________________________________

def text_1():
    text_1 = open('text_1.txt', encoding='utf-8')
    keys = text_1.readlines()
    text_1.close()
    return keys
    
def text_2():
    text_2 = open('text_2.txt', encoding='utf-8')
    meaning = text_2.readlines()
    text_2.close()
    return meaning

def get_dictionary(keys, meaning):
    keys = [line.rstrip() for line in keys]
    meaning = [line.rstrip() for line in meaning]
    dictionary = dict(zip(keys, meaning))
    return dictionary

def script_bot(dictionary):
    a = None
    print('Введите текст, чтобы начать.\nЧтобы завершить программу введите "пока".')
    while a != 'пока':
        a = input('').lower()
        for i in dictionary:
            if i == a:
                print(dictionary[i])
                break   
        if i != a:
            print('Я не знаю что на это ответить. Может ты подскажешь?')
            b=dictionary[a] = input()
            text_1 = open('text_1.txt', 'a',encoding='utf-8')
            text_1.writelines(f'\n{a}')
            text_2 = open('text_2.txt', 'a', encoding='utf-8')
            text_2.writelines((f'\n{b}'))
            text_1.close()
            text_2.close()

a = text_1()
b = text_2()
c = get_dictionary(a,b)
d = script_bot(c)
print(d)
