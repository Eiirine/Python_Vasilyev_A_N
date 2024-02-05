# Задание 1
print("Задание №1")
day = input("Введите день: ")
month = input("Введите месяц: ")
print(f"Текущий день: {day}, текущий месяц: {month}")

# Задание 2
print("Задание №2")
current_year = int(input("Введите текущий год: "))
birth_year = int(input("Введите год рождения: "))
age = current_year - birth_year
print(f"Ваш возраст: {age} лет")

# Задание 3
print("Задание №3")
miles = float(input("Введите расстояние в милях: "))
kilometers = miles * 1.6
print(f"{miles} миль равно {kilometers} километров")

# Задание 4
print("Задание №4")
size = int(input("Введите размер списка: "))
powers_of_two = [2 ** i for i in range(size)]
print("Список степеней двойки:", powers_of_two)

# Задание 5
print("Задание №5")
size = int(input("Введите размер списка: "))
numbers = [5 * k + 3 for k in range(size)]
print("Прямой порядок:", numbers)
print("Обратный порядок:", numbers[::-1])

# Задание 6
print("Задание №6")
number = int(input("Введите число: "))
if number % 3 == 0:
    print(f"{number} делится на 3")
else:
    print(f"{number} не делится на 3")

# Задание 7
print("Задание №7")
number = int(input("Введите число: "))
if number >= 0:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Факториал {number}! равен {factorial}")
else:
    print("Введите положительное число")

# Задание 8
print("Задание №8")
n = int(input("Введите количество чисел в последовательности: "))
fibonacci_sequence = [1, 1]
for i in range(2, n):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
print("Последовательность Фибоначчи:", fibonacci_sequence)

# Задание 9
print("Задание №9")


def second_largest(numbers):
    sorted_numbers = sorted(set(numbers), reverse=True)
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]
    else:
        return None


# Пример использования:
numbers_list = [5, 2, 8, 1, 7, 3]
result = second_largest(numbers_list)
print("Второе по величине число:", result)

# Задание 10
print("Задание №10")


def sum_of_odd_numbers(count):
    return sum(range(1, 2 * count, 2))


# Пример использования:
count_numbers = int(input("Введите количество чисел: "))
result_sum = sum_of_odd_numbers(count_numbers)
print(f"Сумма нечетных чисел: {result_sum}")
