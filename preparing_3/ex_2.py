# Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.


def num_comparing(number):
    try:
        result = float(number)
        if int(result) == result:
            print('Это число целое')
        else:
            print('Это число дробное')
            left, right = str(result).split('.')
            return left == right
    except ValueError:
        print('Попросили же ввести число. Попробуйте снова.')


print(num_comparing(input('Введите число: ')))


