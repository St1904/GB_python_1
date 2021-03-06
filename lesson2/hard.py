# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

k = float(equation[equation.index('= ') + 2:equation.index('x')])
b = float(equation[equation.index('+ ') + 2:])
result = k * x + b
print(result)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date1 = '01.22.1001'
date2 = '1.12.1001'
date3 = '-2.10.3001'

def date_correct(s):
    month_31 = [1, 3, 5, 8, 10, 12]
    spl = s.split('.')
    if len(spl) != 3:
        return False
    day = spl[0]
    month = spl[1]
    year = spl[2]
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False
    if not day.isdigit or not month.isdigit or not year.isdigit:
        return False
    is_31_days = True if int(month) in month_31 else False
    if ((is_31_days and 1 <= int(day) <= 31) or (not is_31_days and 1 <= int(day) <= 30)) \
            and 1 <= int(month) <= 12 and 1 <= int(year) <= 9999:
        return True
    else:
        return False

print(date_correct(date))
print(date_correct(date1))
print(date_correct(date2))
print(date_correct(date3))
print(date_correct('ofhef'))
print(date_correct('01.12.2018.35'))
print(date_correct('01.12.0000'))
print(date_correct('31.12.2018'))



# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3