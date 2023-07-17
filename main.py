pole = [
    ['0', '*', '#', '$', '*'],
    ['#', '*', '#', '*', '*'],
    ['*', '*', '#', '#', '*'],
    ['*', '#', '*', '#', '*'],
    ['*', '*', '*', '*', '*'],
]

# Ось по вертикали
pole_x = 0
# Ось по горизонтали
pole_y = 0
command = ""

for step_ryad in pole:
    for step_elem in step_ryad:
        print(step_elem, end=" ")
    print()
command_user = input("Введите команду: ")

while command_user != "выход":
    if command_user == "вперед":
        if pole_y < 4 and pole[pole_x][pole_y + 1] != "#":
            pole[pole_x][pole_y] = "*"
            pole_y += 1
            pole[pole_x][pole_y] = "0"

    elif command_user == "назад":
        if pole_y > 0 and pole[pole_x][pole_y - 1] != "#":
            pole[pole_x][pole_y] = "*"
            pole_y -= 1
            pole[pole_x][pole_y] = "0"

    elif command_user == "вниз":
        if pole_x < 4 and pole[pole_x + 1][pole_y] != "#":
            pole[pole_x][pole_y] = "*"
            pole_x += 1
            pole[pole_x][pole_y] = "0"

    elif command_user == "вверх":
        if pole_x > 0 and pole[pole_x - 1][pole_y] != "#":
            pole[pole_x][pole_y] = "*"
            pole_x -= 1
            pole[pole_x][pole_y] = "0"

    else:
        print("Нет такой команды!")

    for step_ryad in pole:
        for step_elem in step_ryad:
            print(step_elem, end=" ")
        print()
    if pole_x == 0 and pole_y == 3:
        print("Победа")
        break
    command_user = input("Введите команду: ")

print("Game over!")
