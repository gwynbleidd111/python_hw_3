Задача №1___________________________________________________________

def get_number():
    n = int(input("Введите число: "))
    return n

def fibo(n):
    list =[]

    if n == 1:
        list = [1]
    elif n == 2:
        list = [1,1]
    else:    
        list = [1,1]
        fib_1 = fib_2 = 1
        for i in range(2, n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            list.append(fib_2)
    return list     

def transformation(list):
    list_1 = [str(x) for x in list]
    new_list = ' '.join(list_1)  
    return new_list

def write(list):
    data = open("text.txt", "w")
    data.writelines(list)
    data.close()

n = get_number()
a = fibo(n)
b = transformation(a)
write(b)
