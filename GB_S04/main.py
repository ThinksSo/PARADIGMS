# Нормализация данных
# Реализовать с использованием функциона ьной парадигмы процедуру normalization, 
# которая выполняет нормализацию полученного массива по приведенной формуле 
# нормализованного значения элемента, где
#   х_norm - нормализованное значение элемента 
#   х - исходное значение элемента х_max, 
#   x_min - максимальное и минимальное значение в массиве


def normalize (data):
    min_val = min(data)
    max_val = max(data)

    def normalize_element(x):
        return (x - min_val) / (max_val - min_val)
    
    return list(map(normalize_element, data))



# Фильтрация данных
#  Написать скрипт принимающий на вход массив с данными о людях и число - возраст, 
# а возвращающий число - количество люоей старше указанного возраста.


people = [
{'name': 'Elizaveta', 'age': 35},
{'name': 'Vasiliy', 'age': 69},
{ 'name': 'Sergey', 'age': 20},
{'name': 'Ivan', 'age': 8} 
]


def filter_by_age (people:list, min_age: int) -> list:
    return list(filter(lambda pers: min_age <= pers ['age'], people))

age = 30
filtered_people = filter_by_age(people, age)
print(filtered_people)
print(len(filtered_people))


# Поиск дубликатов
# Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. 
# На вход подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). 
# При применении к массиву, дубликаты должны быть выведены на экран в виде списка.


def find_duplicates(numbers):
    unique_numbers = set ()
    return list(filter(lambda x: x in unique_numbers or 
                       unique_numbers .add(x), numbers))

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 6]
duplicates = find_duplicates(numbers)
