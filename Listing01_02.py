# Задание 1
print("Задание №1")
number = int(input("Введите целое число: "))
digit_count = [0] * 10

while number > 0:
    digit = number % 10
    digit_count[digit] += 1
    number //= 10

for i in range(10):
    print(f"Цифра {i} встречается {digit_count[i]} раз")

# Задание 2
print("Задание №2")
number = int(input("Введите целое число: "))
result = 0

while number > 0:
    digit = number % 10
    result = result * 10 + (9 - digit)
    number //= 10

print("Результат:", result)

# Задание 3
print("Задание №3")
numbers = [12, 3, 456, 78]
result = int("".join(map(str, numbers)))
print("Результат:", result)

# Задание 4
print("Задание №4")
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 == list2:
    print("Списки равны")
else:
    print("Списки не равны")

# Задание 5
print("Задание №5")
numbers = [2, 5, 6]
upper_limit = 10
result = sum(set(range(1, upper_limit + 1)) - set(numbers))
print("Сумма:", result)

# Задание 6
print("Задание №6")
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a + b > c and b + c > a and a + c > b:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

# Задание 7
print("Задание №7")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if b - a == c - b:
    print("Числа образуют арифметическую последовательность")
else:
    print("Числа не образуют арифметическую последовательность")

# Задание 8
print("Задание №8")
day_number = int(input("Введите число от 1 до 7: "))
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

if 1 <= day_number <= 7:
    print("День недели:", days_of_week[day_number - 1])
else:
    print("Неверный ввод")

# Задание 9
print("Задание №9")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result = num1 if num1 > num2 else num2 if num2 > num1 else "Числа равны"
    print("Большее число:", result)

except ValueError:
    print("Ошибка ввода. Введите действительные числа.")

# Задание 10
print("Задание №10")
try:
    A = float(input("Введите значение A: "))
    B = float(input("Введите значение B: "))

    if A != 0:
        x = (B - 1) / A - 1
        print("Решение уравнения:", x)
    elif A == 0 and B == 1:
        print("Уравнение имеет бесконечно много решений")
    else:
        print("Уравнение не имеет решений")

except ValueError:
    print("Ошибка ввода. Введите действительные числа.")
except ZeroDivisionError:
    print("Ошибка деления на ноль. Введите значение A, отличное от нуля.")
