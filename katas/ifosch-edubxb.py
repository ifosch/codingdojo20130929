import unittest
from mock import Mock

MySQLdb = Mock()
db = Mock()
USER = 'User'
PASSWD = 'Passwd'


class Test_Llibre(unittest.TestCase):
    def setUp(self):
        db.query = Mock()
        MySQLdb.connect = Mock(return_value=db)
        MySQLdb.OperationalError = Exception

    def test_creacio(self):
        titol1 = 'titol1'
        autor1 = 'autor1'
        llibre1 = Llibre(titol1, autor1)
        db.data = {'titol': 'titol1', 'autor': 'autor1'}
        MySQLdb.connect.assert_called_once_with(
            USER,
            PASSWD
        )
        db.query.assert_called_once_with(
            """ SELECT * FROM llibres WHERE titol = %s AND autor = %s """,
            (
                titol1,
                autor1
            )
        )

    def test_connection_timeout(self):
        MySQLdb.connect.side_effect = MySQLdb.OperationalError(
            2006,
            'Mysql Has Gone Away'
        )
        llibre1 = Llibre('titol1', 'autor1')
        self.assertRaises(MySQLdb.OperationalError, MySQLdb.connect)


class Llibre(object):
    def __init__(self, titol, autor):
        try:
            db = MySQLdb.connect(USER, PASSWD)
        except MySQLdb.OperationalError:
            pass
        else:
            db.query(
                """ SELECT * FROM llibres WHERE titol = %s AND autor = %s """,
                (
                    titol,
                    autor
                )
            )

if __name__ == "__main__":
    unittest.main()
