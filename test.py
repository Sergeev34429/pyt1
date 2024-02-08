import random
pass1 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 

lenn = int(input("Введите длину пароля: "))

password = ""

for i in range(lenn):
    password += pass1[random.randint(0,len(pass1))]
print(password)