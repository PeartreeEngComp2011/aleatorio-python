import random

number = random.randint(0,10)

print(number)

#Forçando para dar sempre o mesmo resultado

random.seed(1)

print(number)

#Escolhendo a partir de uma lista

lista = [3,12,7,9]

number2 = random.choice(lista)

print(number2)