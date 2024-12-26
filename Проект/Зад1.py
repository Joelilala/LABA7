def count_zeros_and_indices(input_list):
    """Подсчитывает количество нулевых элементов и выводит их индексы."""
    zero_count = 0
    zero_indices = []

    for index, value in enumerate(input_list):
        if value == 0:
            zero_count += 1
            zero_indices.append(index)

    return zero_count, zero_indices

# Ввод данных
input_list = [1, 0, 2, 0, 3, 0, 4]  # Пример списка

# Подсчет нулевых элементов и получение их индексов
count, indices = count_zeros_and_indices(input_list)

# Вывод результата
print(f"Количество нулевых элементов: {count}")
print(f"Индексы нулевых элементов: {indices}")
