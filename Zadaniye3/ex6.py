x1 = int(input("Введите значение первой клетки по горизонтали:(от 1 до 8) "))
y1 = int(input("Введите значение первой клетки по вертикали:(от 1 до 8) "))
x2 = int(input("Введите значение второй клетки по горизонтали:(от 1 до 8) "))
y2 = int(input("Введите значение второй клетки по вертикали:(от 1 до 8) "))
def add():

    if (x1 >= 9 or x1 < 1) or (x2 >= 9 or x2 < 1) or (y1 >= 9 or y1 < 1) or (y2 >= 9 or y2 < 1):
        print("Неверна введена одна из переменных")
    else:
        if (x1 + y1) % 2 == (x2 + y2) % 2 :
            print("Да")
        else:
            print("Нет")    
add()
       