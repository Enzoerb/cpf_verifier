import unittest
import validacpf_enzo
from random import randint


class TestCpfValidation(unittest.TestCase):

    def test_retira_formatacao(self):
        funcao = validacpf_enzo.retira_formatacao
        self.assertEqual(funcao("111.111.111-11"), "11111111111")
        self.assertEqual(funcao("123456789-01"), "12345678901")
        self.assertEqual(funcao("99234678824"), "99234678824")
        self.assertEqual(funcao("12.34.56.87.9-01"), "12345687901")

    def test_check_first_digit(self):
        funcao = validacpf_enzo.check_first_digit

        with self.assertRaises(ValueError):
            funcao("735.412.830-92")

        self.assertTrue(funcao("12345678909"))
        self.assertTrue(funcao("1234567890"))
        self.assertTrue(funcao("12345678908"))
        self.assertTrue(funcao("12345678904567"))
        self.assertTrue(funcao("12345678904"))
        self.assertFalse(funcao("12345678919"))
        self.assertFalse(funcao("123456789109"))
        self.assertFalse(funcao("12345678980"))

        self.assertTrue(funcao("73541283092"))
        self.assertTrue(funcao("73541283090"))
        self.assertTrue(funcao("735412830924567"))
        self.assertTrue(funcao("73541283095672"))
        self.assertTrue(funcao("73541283094567"))
        self.assertFalse(funcao("73541283045692"))
        self.assertFalse(funcao("73541283082"))

    def test_check_second_digit(self):
        funcao = validacpf_enzo.check_second_digit

        with self.assertRaises(ValueError):
            funcao("123.456.789-09")

        self.assertTrue(funcao("12345678909"))
        self.assertTrue(funcao("12345678941"))
        self.assertFalse(funcao("12345678929"))
        self.assertFalse(funcao("12345678908"))
        self.assertFalse(funcao("12345678954"))
        self.assertFalse(funcao("12345678904"))

        self.assertTrue(funcao("73541283092"))
        self.assertTrue(funcao("73541283050"))
        self.assertTrue(funcao("735412830922222"))
        self.assertFalse(funcao("73541283022"))
        self.assertFalse(funcao("73541283098"))
        self.assertFalse(funcao("7354128309456788"))
        self.assertFalse(funcao("73541283045678998"))

    def test_valida_cpf(self):
        funcao = validacpf_enzo.valida_cpf
        self.assertTrue(funcao("123.456.789-09"))
        self.assertFalse(funcao("123.456.789-19"))
        self.assertFalse(funcao("123.456.789-05"))
        self.assertFalse(funcao("123.456.789-24"))

        self.assertTrue(funcao("735.412.830-92"))
        self.assertTrue(funcao("735412830-92"))
        self.assertTrue(funcao("73541283092"))
        self.assertFalse(funcao("735.412.830-09"))
        self.assertFalse(funcao("735.412.830-22"))
        self.assertFalse(funcao("735412830-22"))
        self.assertFalse(funcao("73541283099"))
        self.assertFalse(funcao("735412830-99"))
        self.assertFalse(funcao("735.412.830-99"))

        for i in range(10):
            generated = [str(randint(0, 9)) for _ in range(i)]
            self.assertFalse(funcao("".join(generated)))
        for i in range(0, 9):
            self.assertFalse(funcao("{i}"*11))


if __name__ == '__main__':
    unittest.main()
