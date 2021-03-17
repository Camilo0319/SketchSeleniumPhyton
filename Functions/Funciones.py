from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.common.action_chains import ActionChains
class Funciones():

#----------------------------INICIO ENTORNOS ---------------------------

    EntornoFranciaVersionSeis="https://212.83.164.238/ctv6/login/login.html"
    EntornoEspañaVersionSeis="http://192.168.204.219:9080/chronotime/index.html"
    GooglePage="https://www.spotify.com/es/"

#--------------------------- FIN DE ENTORNOS --------------------------


#--------------------------------------------LOGUEARSE EN LA APLICACION--------------------------
    def login(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Drivers\geckodriver.exe")
        self.driver.get(self.GooglePage)
        time.sleep(5)
        #self.driver.find_element_by_id(Elementoslogin.Login.user_id).send_keys("CMLAutt")
        #profile = webdriver.FirefoxProfile()
        #profile.accept_untrusted_certs = True

    def cerrarAplicacion(self):
        self.driver.close()



#------------------------------------------------FIN DE LOGUEARSE -------------------------------
#----------------------------------------------FUNCIONES PARA CLIQUEAR----------------------------
    def clicElementoID(self,elemento):
        self.driver.find_element_by_id(elemento).click()

    def clicElementoXpath(self,elemento):
        self.driver.find_element_by_xpath(elemento).click()

    def clicElementoCSS(self,elemento):
        self.driver.find_element_by_class_name(elemento).click()
#----------------------------------------------FIN  PARA CLIQUEAR----------------------------

#----------------------------------------------VERIFICACION DE ELEMENTOS------------------------

    def verificarTextosXpath(self,elemento):
        elemento=self.driver.find_element_by_xpath(elemento)
        print(elemento.text)

    def verificarElementoSeVisualiza(self,elemento):
        self.driver.find_element_by_xpath(elemento).is_enabled()

    def verificarElementoSeVisualizaClase(self,elemento):
        self.driver.find_element_by_class_name(elemento).is_enabled()




#------------------------------DESPLAZAR EN ELEMENTOS----------------------------------------------
    def desplazarRatonporxPath(self, elemento):
        element_hover = self.driver.find_element_by_xpath(elemento)
        hover = ActionChains(self.driver).move_to_element(element_hover)
        hover.perform()


#------------------------------ESPERASS-------------------------------------

    def esperaImplicita(self,tiempodeespera):
        driver=self.driver
        driver.implicitly_wait(tiempodeespera)


    def esperaExplicitaXpath(self,elemento):
        wait=WebDriverWait(self.driver,20)
        wait.until(EC.element_to_be_clickable(By.XPATH,elemento))


#--------------------REDIMENSIONAR PANTALLA---------------------------------------------------------------------------

    def redimensionarPantalla(self,ancho,alto):
        self.driver.set_window_size(ancho,alto)


#-------------------FIN DE REDIMENSIONAR LA PANTALLA------------------------------------------------------------------

#--------------------ITERACCIONES DEL NAVEGADOR ---------------------------------------------------------------------

    def refrescarPagina(self):
        self.driver.refresh()

#----------------------FIN DE LAS ITERRACIONES DEL NAVEGADOR---------------------------------------------------------
#-----------------------INICIO ITERACCIONES DEL TECLADO -------------------------------------------------------------

    def tabularTeclado(self,element,accion):
        if accion=="TAB":
            element=self.driver.find_element_by_xpath(element).send_keys(Keys.TAB)
        elif accion=="FLECHADERECHA":
            element=self.driver.find_element_by_xpath(element).send_keys(Keys.ARROW_RIGHT)

    def escribirTexto(self,elementoSeleccionado,texto):
        elemento=self.driver.find_element_by_class_name(elementoSeleccionado)
        elemento.send_keys(texto)





#-----------------------FIN DE ITERACCIONES DEL TECLADO--------------------------------------------------------------