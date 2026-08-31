from random import randint

number = randint(1,20)
attempts = 1
while attempts > 0:
	if attempts > 5: break
	attempts_left = 5 - attempts 
	guess = int(input(f"Попытка {attempts}. Введите число: "))
	if guess == number:
		print("Угадал!")
	elif guess > number:
		print(f"Много! Осталось попыток: {attempts_left}")
	else: 
		print(f"Мало! Осталось попыток: {attempts_left}")
	attempts += 1
