####################
Coding Dojo Setembre
####################

Informació pel coding dojo
==========================

Definició
---------

Un test double és un element de codi que es fa servir en un test, per testejar-ne un altre element. El seu nom ve dels stunt doubles, especialistes en cinema que doblen l'actor en les escenes amb alguna complexitat.

Motius
------

El motiu principal és la depedència del codi que es vol testejar d'altres elements:

* No són disponibles
* Són indeterministes
* Són massa complicats de configurar per cada test
* Impliquen recursos no disponibles en fer els tests

Tipus
-----

* Dummy
    L'element no s'utilitza mai, només es fa servir per completar el pas de
    paràmetres.
* Fake
    L'element es pot utilitzar, però les seves respostes no contenen la lògica
    requerida per producció.
* Stub
    L'element s'utilitza, sense que hi hagi la lògica implementada, però solen
    recollir informació sobre les crides que se'ls hi fa.
* Mock
    S'utilitzen per verificar-ne el comportament d'una forma menys laboriosa
    que un stub. Es crea l'element, es configura per donar les respostes
    corresponents i, un cop fet el test, es valida que n'ha tingut les crides
    corresponents.

Exemple: Dummy
--------------

El codi que es vol testejar requereix paràmetres peró no s'utilitzen: ::

    BCN = 'Barcelona'
    MAD = 'Madrid'

    class TestCarMovement(unittest.TestCase):

        def setUp(self):
            self.car = Car(city=BCN)

Exemple: Dummy (II)
-------------------

::

    def test_travel(self):
            self.assertEquals(self.car.city, BCN)
            self.car.goesTo(MAD)
            self.assertEquals(self.car.city, MAD)

Exemple: Fake
-------------

El codi que es vol testejar necessita que un altre element respongui d'una manera determinada: ::

    class gps(object):

        def validate(self, location, city):
            return city == BCN

Exemple: Fake (II)
------------------

::

    class TestCarLocation(unittest.TestCase):

        def setUp(self):
            self.gps = gps()
            self.car1 = Car(location=(46, 40), city=BCN)
            self.car2 = Car(location=(46, 40), city=MAD)

Exemple: Fake (III)
-------------------

::

        def test_GPS(self):
            self.assertTrue(self.gps.validate(
                self.car1.location,
                self.car1.city))
            self.assertFalse(self.gps.validate(
                self.car2.location,
                self.car2.city))

Exemple: Stub
-------------

El codi té lógica implementada per controlar les crides que se'ls hi fa: ::

    class Garage(object):

        def __init__(self):
            self.count = 0

        def repair(self, car):
            self.count += 1

Exemple: Stub (II)
------------------

::

    class TestCarTechCheck(unittest.TestCase):

        def setUp(self):
            self.garage = Garage()
            self.car1 = Car()
            self.car2 = Car(kms=10000)

        def test_addKms(self):
            self.car1.addKms(10000)
            self.car2.addKms(5000)
            self.assertEquals(self.garage.count, 1)

Exemple: Mock
-------------

El test valida el comportament: ::

    from unittest.mock import Mock

    class TestCarTechCheck2(unittest.TestCase):

        def setUp(self):
            self.garage = Mock()
            self.garage.repair = Mock()
            self.car1 = Car(garage=self.garage)
            self.car2 = Car(garage=self.garage, kms=10000)

Exemple: Mock (II)
------------------

::

        def test_addKms(self):
            self.car1.addKms(10000)
            self.car2.addKms(5000)
            self.garage.repair.assert_called_once_with(self.car2)

Enllaços
--------

* `Mocks Aren't Stubs`_, de Martin Fowler
* `The role of Mocking in TDD, Test First with Rhino Mocks, KandaAlpha`_, de Will Beattie
* `Introducción a los Tests Unitarios, TDD y Mocking`_, de Juan García Ramona

Preguntes
---------

Gràcies!

.. _`Mocks Aren't Stubs`: http://martinfowler.com/articles/mocksArentStubs.html
.. _`The role of Mocking in TDD, Test First with Rhino Mocks, KandaAlpha`: http://blog.willbeattie.net/2009/07/role-of-mocking-in-tdd-test-first-with.html
.. _`Introducción a los Tests Unitarios, TDD y Mocking`: http://juan-garcia-carmona.blogspot.com.es/2012/09/introduccion-los-tests-unitarios-tdd-y.html
