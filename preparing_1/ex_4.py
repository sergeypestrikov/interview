# Написать программу «Банковский депозит».
# Она должна состоять из функции и ее вызова с аргументами.
# Клиент банка делает депозит на определенный срок.
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
# Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
# Каждый из трех банковских продуктов должен быть представлен в виде словаря
# с ключами (begin_sum, end_sum, 6, 12, 24). Ключам соответствуют значения начала
# и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
# В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов
# и выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.


deposite_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
deposite_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5}
deposite_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
all_deposits = [deposite_1, deposite_2, deposite_3]

def total_result(summ, term):
    final_result = 0
    try:
        for deposite in all_deposits:
            if deposite['begin_sum'] <= summ < deposite['end_sum']:
                final_result = summ
                percent = deposite[term] / 100

                final_result += summ * percent * (term / 12)
        if not final_result:
            raise ValueError('Неверная сумма вклада')
        return final_result
    except KeyError as e:
        return f'Неправильный срок вклада. KeyError {e}'
    except ValueError as e:
        return e


print(total_result(1000, 12))
print(total_result(100000, 4))