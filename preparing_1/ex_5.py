# Усовершенствовать программу «Банковский депозит».
# Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
# Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
# Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
# Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
# Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
# а главная функция — общую сумму по вкладу на конец периода.

deposite_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
deposite_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5}
deposite_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
all_deposits = [deposite_1, deposite_2, deposite_3]


def total_result(summ, term, additional):

    def additional_money():
        nonlocal additional, term
        additional += (additional * percent *((term - 2 ) / 12))
        return additional * (term - 2)

    final_result = 0
    try:
        for deposite in all_deposits:
            if deposite['begin_sum'] <= summ < deposite['end_sum']:
                final_result = summ
                percent = deposite[term] / 100

                final_result += summ * percent * (term / 12)
                final_result += additional_money()
        if not final_result:
            raise ValueError('Неверная сумма вклада')
        return final_result
    except KeyError as e:
        return f'Неправильный срок вклада. KeyError {e}'
    except ValueError as e:
        return e


print(total_result(1000, 12, 1000))
print(total_result(100000, 4, 1000))