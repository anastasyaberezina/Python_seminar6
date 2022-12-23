# Cоздать список из строк. Проверить, присутствует ли в списке число.

list = ['blue', 'r3d','gre2n', 'hello']

list = ''.join([str(i) for i in list])
print(list)

n = input('Введите значение: ')

res = sum(map(lambda x: 1 if x == 'n' else 0, list)) # Что то не работает?
print(res)

