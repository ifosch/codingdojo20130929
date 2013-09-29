import unittest
from mock import Mock


class Car(object):
    def __init__(self, kms=0, garage=None):
        self.kms = kms
        self.garage = garage

    def addKms(self, kms):
        self.kms += kms
        if self.garage is not None and self.kms > 15000:
            self.garage.repair(self)


class Test(unittest.TestCase):
    def setUp(self):
        self.garage = Mock()
        self.garage.repair = Mock()
        self.car1 = Car(garage=self.garage)
        self.car2 = Car(garage=self.garage, kms=10000)

    def test(self):
        self.car1.addKms(10000)
        self.car2.addKms(10000)
        self.garage.repair.assert_called_once_with(self.car2)

if __name__ == '__main__':
    unittest.main()
