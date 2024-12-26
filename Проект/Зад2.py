# Пример списка вещественных чисел
numbers = [-3.5, 2.1, -4.0, 5.6, -1.2, 3.3, -7.8, 0.0]

# 1. Нахождение максимального по модулю элемента списка
max_abs_element = max(numbers, key=abs)
print("Максимальный по модулю элемент:", max_abs_element)

# 2. Нахождение суммы элементов между первым и вторым положительными элементами
first_positive_index = None
second_positive_index = None

for i, num in enumerate(numbers):
    if num > 0:
        if first_positive_index is None:
            first_positive_index = i
        elif second_positive_index is None:
            second_positive_index = i
            break

if first_positive_index is not None and second_positive_index is not None:
    sum_between = sum(numbers[first_positive_index + 1:second_positive_index])
    print("Сумма элементов между первым и вторым положительными элементами:", sum_between)
else:
    print("Недостаточно положительных элементов для вычисления суммы.")