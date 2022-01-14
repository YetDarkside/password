import random

symbols = '+-/*!&$№%^*()#.|?=@<>[]{}abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
num = input('кол-во паролей?'+ "\n")
length = input('Длина пароля?'+ "\n")
num = int(num)
length = int(length)
for n in range(num):
    password =''
    for i in range(length):
        password += random.choice(symbols)
    print(password)