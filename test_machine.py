from translator import translator
from machine import machine
import unittest


class MachineTest(unittest.TestCase):
    """ 处理器测试 """

    def setUp(self) -> None:
        print("Test beginning:")

    def tearDown(self) -> None:
        print("Test finished.")

    def test_hello(self):
        print("Testing hello")
        translator.translate("./asm/hello.asm", "./asm/target")
        result = machine.start("./asm/target", '')
        self.assertEqual(result, "Hello,world")

    def test_cat(self):
        print("Testing cat")
        translator.translate('./asm/cat.asm', './asm/target')
        result = machine.start('./asm/target', './asm/cat_test.txt')
        text = ''
        with open('asm/cat_test.txt') as f:
            text = f.read()
        self.assertEqual(result, text)

    def test_prob1(self):
        print("Testing prob1")
        translator.translate("./asm/prob1.asm", "./asm/target")
        result = machine.start("./asm/target", '')
        print("问题1答案：" + result)
        self.assertEqual(int(result), sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))

if __name__ == '__main__':
    unittest.main()
