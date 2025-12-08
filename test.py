def task_1():
    massive = [["Строка №", "Столбец 1", "Столбец 2", "Столбец 3", "Столбец 4", "Столбец 5"],
            ["1", "folder", "coursework.doc", "folder", "pict.png", "data.accdb"],
            ["2", "icon.ico", "script.js", "index.html", "style.css", "prog.py"],
            ["3", "my_song.mp3", "anapa-2003.jpg", "cs_1.6.exe", "folder", "cheat.txt"],
            ["4", "notes.txt", "main.py", "work.pdf", "cartoon.mp4", "array.py"],
            ["5", "project.psd", "cycle.py", "folder", "cycle.js", "turtle.py"]]

    def print_massive(text):
        print(f"\n{text}")
        for i in range(len(massive)):
            print(massive[i])

    print_massive("Начальный список")

    massive_py = []
    massive_js = []
    for t in range(6):
        for i in range(6):
            if massive[t][i] == "folder": massive[t][i] = ""
            elif massive[t][i] == "data.accdb": massive[t][i] = "data.sql"
            elif massive[t][i][-3:] == ".py": massive_py.append(massive[t][i])
            elif massive[t][i][-3:] == ".js": massive_js.append(f"new_{massive[t][i]}")

    print_massive("без папок и с заменой data")
    print(f"\nвсе файлы.py\n{massive_py}")
    print(f"\nвсе new_файлы.js\n{massive_js}")


# задание 2

def task_2():
    word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    inp = int(input("Введите число от 0 до 9: "))
    for i in range(inp+1):
        print(word_numb[i])

def task_3():
    bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
    for i in range(len(bin_sy)):
        print(int(bin_sy[i],2))
