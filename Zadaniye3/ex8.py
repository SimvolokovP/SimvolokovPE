a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
def add():
    if a == b == c:
        print("3")
    elif a == b  or a == c   or c == b:
        print("2")
    else:
        print("0")
add()        