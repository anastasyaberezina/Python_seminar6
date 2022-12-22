# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите число: ')
lst = num.split()
print(*lst)

res=[]
for i in lst:
        res.append(sum(map(int, str(i))))
print (*res)


