import unittest

from src.X import X


class XTest(unittest.TestCase):

    def test01(self):
        x = X("config.txt")
        configObj = x.read_config_path()
        self.assertNotEqual('', configObj.get('credentials', 'email'))

    def test02(self):
        x = X("config.txt")
        configObj = x.read_config_path()
        self.assertNotEqual('', configObj.get('credentials', 'password'))


if __name__ == "__main__":
    unittest.main()
