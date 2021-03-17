import unittest
from Functions import  Funciones
from PageLocators import  LoginPage as PaginaPrincipal


# Objeto que permite llamar todas las funciones
hazEl=Funciones.Funciones()
class Plantilla(unittest.TestCase):


    def setUp(self) :
        hazEl.login()




    def test06(self):
        hazEl.clicElementoXpath(PaginaPrincipal.PaginaPrincipal.texto_Premium_xpath)


    def tearDown(self):
        hazEl.cerrarAplicacion()



if __name__ == '__main__':
    unittest.main()