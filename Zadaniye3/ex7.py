def add():
    n = int(input("Введите номер года: "))
    if (n % 4 ==0 and n % 100 != 0) or (n % 400 == 0):
        print("Да, этот год - високосный")
    else:
        print("Нет, год - не високосный")   
add()         
