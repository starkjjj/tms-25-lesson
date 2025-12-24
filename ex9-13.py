user_numbers_1 = input("Введите первое число для поиска их произведения и ср.арифметического ")
user_numbers_2 = input("Введите второе число для поиска их произведения и ср.арифметического ")
user_num = input("Введите цифру ")
user_word= input("Введите слово ")

print ("-----")
# ex9
sum = int(user_numbers_1) * int(user_numbers_2)
print (f"Произведение двух чисел равно: {sum}")

# ex10
print(f"Первая буква вашего слова: {user_word[0]}")

# ex11
square = int(user_num) ** 2
print (f"Квадарт вашего числа равен: {square}")

# ex12
print ("Таблица умножения для вашей цифры")
for i in range  (1,11):
    mult = int(user_num) * i
    print (mult)

# ex13
print ("Среднее арифметическое для ваших чисел")
mean = (int(user_numbers_1) + int(user_numbers_2)) / 2
print (mean)
