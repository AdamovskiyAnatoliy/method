import math #Imports a module math that provides extensive functionality for working with numbers.
print("Програма для розрахунку виразу: exp(x)-(y**2+12*x*y-3*x**2)/(18*y-1))")
print("Роботу виконала студентка КМ-71 Нікітіна М.А.")
print("Варіант №19")     
while True: #while repeating the specified block of code until the condition specified in the loop remains true.

    try: #The try-except construct to handle exceptions
        while True:
            try:
                x = int(input("Введіть x: "))
            except ValueError: #An exception is when the function receives an argument of the correct type, but an invalid value.
                print("Сталася помилка, ви ввели буквенний вираз")
            else: 
                break
        while True:    
            try:
                y = int(input("Введіть y: "))
            except ValueError: #An exception is when the function receives an argument of the correct type, but an invalid value.
                print("Сталася помилка, ви ввели буквенний вираз")
            else:
                break

        print("Обчислити x = ", x, "і для y = ", y)
    
        print("exp(x)-(y**2+12*x*y-3*x**2)/(18*y-1)) = ",math.exp(x)-(y**2+12*x*y-3*x**2)/(18*y-1))
    except ZeroDivisionError: #An exception is when dividing by zero.
        print("Сталося ділення на нуль")
    else:
        q = input("Натисніть q для виходу з програми: ")
        if  q == "q":
            break #The break command stops the execution of the loop and translates the execution of the program to the next line after the loop.