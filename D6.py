def has_digit(password):
	return any(char.isdigit() for char in password)
	
def is_very_long(password):
	return len(password) > 12 

def has_upper_letters(password):
	return any(char.isupper() for char in password)

def has_lower_letters(password):
	return any(char.islower() for char in password)

def has_symbols(password):
	return any(not char.isdigit() and not char.isalpha() for char in password)

def main():
	password = list(input("Введите пароль: "))
	score = 0
	functions = [
		has_digit(password), 
		is_very_long(password), 
		has_upper_letters(password), 
		has_lower_letters(password),
		has_symbols(password),
	]
	for result in functions:
		if result:
			score += 2
	print("Рейтинг пароля:", score)


if __name__ == '__main__':
    main()
