a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
def add():
    if b < a and b < c:
        print("Меньшим оказалось второе число, равное", b)
    if c < a and c < b:
        print("Меньшим оказалось третье число, равное", c)    
    if a < b and a < c:
        print("Меньшем оказалось первое число, равное", a)
 
add()   
