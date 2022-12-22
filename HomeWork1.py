# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


with open ('file.txt', 'r') as file:
    new_list = file.read().split()
                    
new_list = list(map(int, new_list))
print(new_list)  # Считываю список из файла и преобразовываю его в список чисел

list_one = [i for i in range(1, 99, len(new_list))] #Создаю новый список чисел, размером первого списка

print(list_one)

for i in range(len(list_one)):          # Убираю , и ' '
    if i != ' ' and ',':
        list_one.append(i)    
    print (list_one[i])

for i in range(len(new_list)):          # Убираю , и ' '
    if i != ' ' and ',':
        new_list.append(i)    
    print (new_list[i])    

n = int(input('Введите позицию: '))  
a = list_one[n]
b = new_list[n]
res = list(map(lambda a, b: a*b, new_list, list_one))

print(res[n])