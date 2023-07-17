pole = [
    ['0', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
]

pole_x = 0
pole_y = 0
command = ""
while command != "выход":
    for step in pole:
        print(step)
    command = input("Введите команду: ")

    if command == "вперед":
        pass

    if command == "назад":
        pass

    if command == "вверх":
        pass

    if command == "вниз":
        pass

    else:
        print("Нет такой команды!")

print("Game over!")
