Задача №2___________________________________________________________

def get_text():
    text = open('text.txt', encoding='utf-8')
    fruit = text.readlines()
    text.close()
    return fruit

def list_title(list):
    list =  ' '.join([str(x) for x in list]).title()
    return list

def fruit(list):
    letter = input("Введите букву: ").upper()
    text = list
    list_1 = []
    for i in text.split():
        if letter in i:
            list_1.append(i)
    return list_1

def list_lower(list):
    list_1 =  ', '.join([str(x) for x in list]).lower()
    return list_1

a = get_text()
b = list_title(a)
c = fruit(b)
d = list_lower(c)
print(d)
