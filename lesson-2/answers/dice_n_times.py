from random import randint

n = input("Скільки разів підкинути кубик? \n")
n = int(n)

for i in range(n):
    dice_side = randint(1, 6)
    print("Підкидаємо", i + 1, " раз. Випало -" , dice_side)
