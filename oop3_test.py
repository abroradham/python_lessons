import unittest

from oop3 import Shaxs, Talaba, Manzil, Fan

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        ism = 'Sardor'
        familiya = 'Sadriddinov'
        passport = 'FF2340056'
        tyil = 1999
        self.shahs = Shaxs(ism, familiya, passport, tyil)

    def test_get_age(self):
        self.assertEquals(24, self.shahs.get_age(2023))

talaba_manzil = Manzil(23, 'sheroziy', 'Namanagan shahar', 'Namangan')
matematika = Fan('Matematika')

class TalabaTest(unittest.TestCase):
    def setUp(self):
        ism = 'Sardor'
        familiya = 'Sadriddinov'
        passport = 'FF2340056'
        tyil = 1999
        idraqam = '001234F'
        manzil = talaba_manzil
        
        self.talaba = Talaba(ism, familiya, passport, tyil, idraqam, manzil)

    def test_create(self):
        self.assertIsNotNone(self.talaba.fanlar,)
        self.assertIsNotNone(self.talaba.manzil.kocha)
        self.assertEqual(self.talaba.fanlar, [])
    
    def test_get_id(self):
        self.assertEqual(self.talaba.idraqam, self.talaba.get_id())

    def test_fanga_yozil(self):
        self.talaba.fanga_yozil(matematika)
        self.assertEqual(self.talaba.yozilgan_fanlar(), ['Matematika'])
    
    def test_fan_remove(self):
        self.talaba.fan_remove(matematika)
        self.assertEqual(self.talaba.yozilgan_fanlar(), [])


unittest.main()