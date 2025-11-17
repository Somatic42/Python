# Задание 1

first_num = 9
second_num = 7.8
my_str = "start"

print(first_num, second_num, my_str)

first_num = 5.2

print(first_num, type(first_num))

third_num = first_num + second_num

print(third_num, type(third_num))

first_num = first_num + 5
second_num = second_num + first_num

print(first_num, second_num)

second_num = int(second_num)

print(first_num, second_num)

my_str = my_str + "&stop"

print(my_str)

print(my_str * 5)

# Задание 2

path = "C:\\Users\\MainAdmin\\Desktop\\programs"

print(path)

path = path + "\\game.exe"

print(path)

path = "C:\\Users\\MainAdmin\\Desktop\\files"
path = path + "\\picture.png"

print(path)

path = "C:\\Games\\city simulator"

print(path)

error_path = path * 2
print("Error path:", error_path)

# Задание 3

num_1 = 7
num_2 = 10
num_3 = 4
summ = num_1 + num_2 + num_3
print("Сумма всех целых чисел:", summ)

num_1 = 7.9
num_2 = 21.3
num_3 = float(num_3)
summ = num_1 + num_2 + num_3
print("Сумма всех нецелых чисел:", summ)

num_1 = 130
num_2 = 4
num_3 = 2
multiplying = num_1 * num_2 * num_3
print("Умножение всех чисел:", multiplying)

division = (num_1 / num_2) / num_3
print("Деление:", division)

num_1 = 2
num_2 = 3
num_3 = 4
degree = num_1 ** num_2 ** num_3
print("Числа в степени:", degree)

num_1 = 2
num_2 = 8
num_3 = 5
math_result = ((43 + num_1) + (num_2 + 67) - (num_3 * 2)) // 2
print(math_result)


# Практическая №2


# Задание 1

bytes_input = int(input("Введите количество байт: "))
bits_output = bytes_input * 8
print(bits_output)

# Задание 2

print('Электронная книга по программированию на английском языке состоит из S страниц.\n'
      'В среднем на странице C строк по N символов.\n'
      'Используется кодировка UTF-8. Определите объём текстового файла в Кбайтах.')

s = int(input('Введите кол-во страниц: '))
c = int(input('Введите кол-во строк на странице: '))
n = int(input('Введите кол-во символов на странице: '))

print(f'\nЭлектронная книга по программированию на английском языке состоит из {s} страниц.\n'
      f'В среднем на странице {c} строк по {n} символов.\n'
      'Используется кодировка UTF-8. Определите объём текстового файла в Кбайтах.\n')

r1 = s * c * n

r2 = r1 / 1024

print(f'{s} * {c} * {n} = {r1} - Всего символов в книге.')
print(f'{r1} / 1024 = {r2} - Кбайт.')
print(f'Ответ: {r2}.')