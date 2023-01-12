result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        operand=int(input('Введите число'))
    except ValueError:
        print(f'{operand} is not a number. Try again.')
        continue
    operator=input('Введите оператор')
    if operator == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operator == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operator == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operator == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')