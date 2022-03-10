# Домашнє завдання:
#
# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# 3) вывести табличку умножения с помощью цикла while
# 4) переделать первое задание под меню с помощью цикла


# 1) Найти min число в листе

list_of_numbers = [22, 3,5,2,8,2,-23, 8,23,5]

smallest_number = min(list)
print("The smallest number is", smallest_number)

# або

list.sort(reverse=False)
print("The smallest number is", list[0])

# або

smallest = list[0] if list else None

for i in list:
    if i < smallest:
        smallest = i
print("The smallest number is", smallest_number)

# 2) удалить все дубликаты в листе

list_of_numbers = list(set(list_of_numbers))
print(list_of_numbers)

# 3) заменить каждое четвертое значение на "Х"


list_of_numbers_two = [22,3,5,2,8,2,-23,8,23,5]

for index, i in enumerate(list_of_numbers_two):
    if index == 0: continue
    if index % 4 == 0:
        list_of_numbers_two[index] = "X"

print(list_of_numbers_two)