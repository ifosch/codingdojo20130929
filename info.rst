=========================
Coding Dojo sobre Mocking
=========================

.. contents::
.. sectnum::

Què és el mocking?
------------------

El mocking és una tècnica per validar software en la què es simulen parts del sistema amb les que el codi a provar té alguna dependència.
La tècnica consisteix en crear un element que es farà passar per un de real, imitant-ne la interfície (tant en prototipus com en comportament). Aquest element tant pot ser un objecte com una llibrería.

Tipus d'enganys
---------------

* Un doble és un element que és del mateix tipus que el provat.
* Un dummy és un element que s'utilitza per passar-lo entre crides, sense que s'arrivi a utilizar.
* Un element fake és el que ofereix una implementació molt simple de l'element real.
* Un stub és un conjunt de respostes tancades a crides dins del test.
* Un mock és un element pre programat amb les respostes esperades a cada crida.

Stub o Mock?
------------

Amb un stub es preserva i comprova l'estat, mentre que amb un mock es comprova i valida el comportament.

Motius per aplicar-lo
---------------------

* La complexitat de l'aplicació.
* La implementació real podria ser més complexa.
* La implementació real proveeix valors no deterministics.
* La implementació real és massa difícil de configurar per cada test.
* La implementació real no és disponible (codi de tercers, tancat o encara no desenvolupat)
* Escriure'n validacions aïllades és massa difícil.
* Temps per desenvolupament de tests massa limitat.
* Requeriments fluids

Exemples
--------

* Col·laboradors
* Entrada/Sortida
* Fitxer
* Base de dades
