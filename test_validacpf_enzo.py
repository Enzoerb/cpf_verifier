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
