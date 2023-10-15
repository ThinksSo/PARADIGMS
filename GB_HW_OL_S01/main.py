from random import randint


# Task 1: Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для сортировки числа
# в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

print('\n \t S1 Task 1: Sort descending (imperative)')


def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


any_array = [randint(1, 100) for _ in range(5)]
print(any_array)
print(sort_list_imperative(any_array), '\n')


# Task 2: Написать точно такую же процедуру, но в декларативном стиле

print('\n \t S1 Task 2: Sort descending (declarative)')


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


new_array = [randint(1, 100) for _ in range(7)]
print(new_array)
print(sort_list_declarative(new_array), '\n')
