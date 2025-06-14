from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print("Задание №1")
names = [student['first_name'] for student in students]
names_counter = Counter(names)
for name, count in names_counter.items():
    print(f"{name}: {count}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = [student['first_name'] for student in students]
names_counter = Counter(names)
print("Задание №2")
print(f"Самое часто встречающиеся имя - {names_counter.most_common(1)[0][0]}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
names_count = []
for students in school_students:
    names = []
    for student in students:
        names.append(student['first_name'])
    names_count.append(Counter(names))
print("Задание №3")
for i in range(len(names_count)):
    print(f"Самое частое имя в классе {i+1} - {names_count[i].most_common()[0][0]}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
print("Задание №4")
for clas in school:
    boys = 0
    girls = 0
    for student in clas['students']:
        if is_male[(student['first_name'])]:
            boys += 1
        else:
            girls += 1
    print(f"Класс {clas['class']}: девочки {girls}, мальчики {boys}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

print("Задание №5")

max_boys = -1000
max_girls = -1000
for clas in school:
    boys = 0
    girls = 0
    for student in clas['students']:
        if is_male[(student['first_name'])]:
            boys += 1
        else:
            girls += 1
    if boys > max_boys:
        max_boys = boys
        more_boys_clas = clas['class']
    if girls > max_girls:
        max_girls = girls
        more_girls_clas = clas['class']

print(f"Больше всего мальчиков в классе {more_boys_clas}")
print(f"Больше всего девочек в классе {more_girls_clas}")

