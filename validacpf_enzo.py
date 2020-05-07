from sys import argv


def retira_formatacao(num_cpf):
    num_cpf = num_cpf.replace('.', '')
    num_cpf = num_cpf.replace('-', '')
    return num_cpf


def check_first_digit(num_cpf):
    first_9 = num_cpf[:9]
    first_digit = 0
    for index, num in enumerate(first_9):
        first_digit += int(num)*(10-index)
    first_digit *= 10
    first_digit %= 11
    if first_digit == 10:
        first_digit = 0
    first_digit = str(first_digit)
    if first_digit == num_cpf[9]:
        return True
    return False


def check_second_digit(num_cpf):
    first_10 = num_cpf[:10]
    second_digit = 0
    for index, num in enumerate(first_10):
        second_digit += int(num)*(11-index)
    second_digit *= 10
    second_digit %= 11
    if second_digit == 10:
        second_digit = 0
    second_digit = str(second_digit)
    if second_digit == num_cpf[10]:
        return True
    return False


def valida_cpf(num_cpf):
    num_cpf = retira_formatacao(num_cpf)
    if len(num_cpf) != 11:
        return False
    if num_cpf.count(num_cpf[0]) == 11:
        return False
    if not num_cpf.isnumeric():
        return False
    if not check_first_digit(num_cpf):
        return False
    if not check_second_digit(num_cpf):
        return False
    return True


if __name__ == '__main__':
    if len(argv) == 2:
        check = valida_cpf(argv[1])
        print(check)
    else:
        print('Please, Enter a CPF to Validate')
