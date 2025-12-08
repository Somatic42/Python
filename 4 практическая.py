def task_411():
    a = input("Введите число: ")
    if int(a) < 0: print(a[1:])
    elif int(a) == 0: print(1)

def task412():
    a = input("Введите текст: ")
    print('.' in a or ',' in a)

def task413():
    a, b = map(int, input("Введите два числа (a,b): ").split(","))
    if a % 3 == 0 and b % 3 == 0:
        print(True)
    elif a % 3 == 0 or b % 3 == 0:
        print("Одно число делится на 3")
    else:
        print(False)

def task421():
    a = int(input("Введите число: "))
    if a > 100: print("*")
    elif a < 0: return
    else: print("*" * a, end=""), print("")

def task422():
    print(input("Введите текст1: ") == input("Введите текст2: "))

def task423():
    r,g,b = map(int, input("Введите (r,g,b): ").split(","))
    match r,g,b:
        case 0,0,0: print("Чёрный цвет") 
        case 255,255,255: print("Белый цвет") 
        case 255,0,0: print("Красный цвет") 
        case 0,255,0: print("Зелёный цвет") 
        case 0,0,255: print("Синий цвет")
        case _: print("Нет цвета") 

def task431():
    a = int(input("Введите число: "))
    if a > 0: print(a-1, a, a+1)
    else: print(0, 1, 2)

def task432():
    a = input("Введите название файла: ")
    match a[-3:]:
        case "doc": print("Word file")
        case "py": print("питон")
        case "txt": print("текстовый")
        case _: print("нет такого")

def task433():
    a,b,c = map(int, input("Введите длину сторон треугольника (a,b,c): ").split(","))
    if a==b==c: print("равносторонний")
    elif a==b or b==c or a==c: print("равнобедренный")
    else: print("разносторонний")

def task1301():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    print(" ".join(alphabet))

    text = input("Введите текст: ")
    used = ""

    for ch in text:
        if ch in alphabet:
            used += ch
            alphabet = alphabet.replace(ch, "")
    
    print(" ".join(used), " ".join(alphabet))
