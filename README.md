# cpf_verifier
verify if a cpf is vallid.

## validacpf_enzo.py
has the functions you need to validate a cpf

### retira_formatacao
this function removes the '.' and '-' from a string, returning it

ex:

> \>>> retira_formatacao('123.456.789-01')

> 12345678901

> \>>> retira_formatacao('1.2-3.4-5.67.890-1')

> 12345678901

### check_first_digit
this function checks if the first digit(10th number) of a cpf is right

ex:

> \>>> check_first_digit('12345678909')

>True

> \>>> check_first_digit('12345678908')

>True

> \>>> check_first_digit('12345678919')

>False

### check_second_digit
this function checks if the second digit(11th number) of a cpf is right

ex:

> \>>> check_first_digit(12345678909)

>True

> \>>> check_first_digit(12345678941)

>True

> \>>> check_first_digit(12345678904)

>False

### valida_cpf
this functions checks if a given cpf is valid.
It will not be valid if all the numbers are equal, if it is not numeric, if it does not have exactly 11 numbers and if check_first_digit or check_second_digit returns False


## test_validacpf_enzo.py
uses unittest to make sure that all validacpf_enzo's functions are working properly
