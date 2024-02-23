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

    def test03(self):
        x = X("config.txt")
        identifier = x.get_profile_from_url("https://www.facebook.com/profile.php?id=61556176318834")
        self.assertEqual("61556176318834", identifier)

    def test04(self):
        x = X("config.txt")
        identifier = x.get_profile_from_url("https://www.facebook.com/vanesa.morales.3994885")
        self.assertEqual("vanesa.morales.3994885", identifier)

    def test05(self):
        x = X("config.txt")
        identifier = x.get_profile_from_url("https://www.facebook.com/omar.huancabalboa")
        self.assertEqual("omar.huancabalboa", identifier)

if __name__ == "__main__":
    unittest.main()
