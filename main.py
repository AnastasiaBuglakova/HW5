# ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

# def path_name_extension(str_):
#     pos = str_.rfind('/')
#     path_name_extension_tuple = (str_[:pos], str_[pos+1:].split('.')[0], str_[pos:].split('.')[1])
#     return path_name_extension_tuple
#
#
# path = '/Users/anastasiabuglakova/Documents/GEEK/Погружение в Python/HW5/main.py'
# print(path_name_extension(path))


# ✔ Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
# names = ['Joрn', "Mary", "Ivan"]
# salary = [10, 100, 1000]
# award = ['9.25%', '10.5%','25%']
# salary_award_name = {names[i]: round(salary[i] * float(award[i][:-1])/100, 2) for i in range(len(names))}
# print(salary_award_name)


# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibonacci(number):
    numbers = []
    l = number
    # while l > 0:
    for i in range(0, number + 1):
        if i in (0, 1) and l > 0:
            numbers.append(i)
            l -= 1
            print(l)
            yield i
        elif l > 0:
            num = sum(numbers[-2:])
            numbers.append(num)
            l -= 1
            print(l)
            yield num

print(*fibonacci(6))
