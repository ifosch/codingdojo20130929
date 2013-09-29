#!/usr/bin/env python
import unittest
from mock import Mock
from mock import MagicMock

usuari = "usuari"
passw = "passw"

class db(object):
	query=Mock()
	OperationalError=Mock(return_value="2006")

class MySQLdb(object):
	connect=Mock(return_value=db())

class Llibre(object):
	def __init__(self, titol, autor):
		db=MySQLdb.connect(usuari, passw)
		db.query("select *")
	
class Test_llibre(unittest.TestCase):
	def test_creacio(self):
		self.llibre1=Llibre("titol1","autor1")
		MySQLdb.connect.assert_called_once_with(usuari,passw)
		db.OperationalError.assert_called_once_with("2006")
		self.llibre2=Llibre("titol2","autor2")
	
if __name__ == '__main__':
	unittest.main()
