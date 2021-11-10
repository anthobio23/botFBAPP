#/usr/bin/python3

import time
import sys
import selenium
import random as rd
import pandas as pd
import WindowControl as wc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains

# brave-browser
#chromedriver_path = "./chromedriver"
brave_path = "/usr/bin/brave-browser"
#option = webdriver.ChromeOptions()
#option.binary_location = brave_path
# driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)
url = "https://www.facebook.com"

# Firefox
opts = Options()
opts.add_argument("--disable-infobars")
opts.add_argument("start-maximized")
opts.add_argument("--disable-extensions")

# pass the argument 1 to allow & 2 to block
#opts.add_experimental_option("prefs", {
#    "profile.default_content_setting_values.notifications": 2
#    })

PATH = "./geckodriver"
driver = webdriver.Firefox(executable_path=PATH, options=opts)

class publicfacebook:

    def __init__(self, driver, mail, passd):

        self.driver = driver
        self.mail = mail
        self.passd = passd
        pass
 
    def datastore(self):
        data = pd.read_excel("data.xlsx")
        return data

    def test_bs4(self):
        
        """
        esta funcion es de prueba
        """
        from urllib.request import urlopen # libreria de prueba
        
        from bs4 import BeautifulSoup

        html = urlopen(str(driver.current_url))
        bs = BeautifulSoup(html.read(), "html.parser") # objeto eu acepta dos argumentos
           
        nameList = bs.find_all('div', {'class': "discj3wi dati1w0a hv4rvrfc"})
        print(len(nameList))
        pass

    def intro_page(self):

        self.driver.get(url)
        assert len(self.driver.window_handles) == 1
        time.sleep(rd.randint(2.0, 8.0))

        email = self.driver.find_element_by_name('email')
        email.send_keys(self.mail)
        time.sleep(1.5)
        passwd = self.driver.find_element_by_name("pass")
        passwd.send_keys(self.passd)
        time.sleep(2.0)
        self.driver.find_element_by_name("login").click()
        time.sleep(rd.randint(10.0, 11.0))

        try:

            market = self.driver.find_elements_by_xpath('//a[@aria-label="Marketplace"]')
            print(len(market))
            market[0].click()
            time.sleep(rd.randint(4.0, 6.0))

        except exceptions.NoSuchElementException:

            main_published = self.driver.find_elements_by_xpath("//div[@class='bp9cbjyn j83agx80 datstx6m taijpn5t oi9244e8']")
            main_published[2].click()
            time.sleep(rd.randint(2.0, 5.0))

            published = self.driver.find_elements_by_xpath("//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi']")
            published[7].click()
            
        try: 

            published = self.driver.find_element_by_xpath("//a[@aria-label='Crear publicación']")
            published.click() # Crear publicacion nueva
            time.sleep(rd.randint(2.0, 5.0))

        except:

            published = self.driver.find_element_by_xpath("//a[@aria-label='Vender artículo']")
            published.click()
            time.sleep(rd.randint(2.0, 5.0))

        _in = self.driver.find_element_by_xpath('//a[@class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 j83agx80 mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x sn7ne77z hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l k4urcfbm"]')
        _in.click() # venta ropa, accesorios y mas
        time.sleep(rd.randint(2.0, 5.0))

    def insert_details(self):

        # importamos los datos
        ds = self.datastore()
        print("Cantidad de productos a publicar: {}".format(len(ds)))

        for iter in range(20, len(ds)):
           # print("codigo del producto a publicar {}".format(ds.iloc[iter][9]))

        # insertamos imagen
            try:

               div_img = self.driver.find_element_by_xpath('//div[@class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 j83agx80 mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l buofh1pr"]')
               div_img.click()
          
               time.sleep(5)
               keyboard = wc.ControlKeyboard("left", iter)
               keyboard.KEY()

            except (exceptions.ElementNotInteractableException):
            
                print("no se pudo insertar la imagen\n")
                pass
       
        # localizar el formulario del titulo y agregar.
            div_s = self.driver.find_elements_by_xpath("//input[@class='oajrlxb2 rq0escxv f1sip0of hidtqoto e70eycc3 lzcic4wl g5ia77u1 gcieejh5 bn081pho humdl8nn izx4hr6d oo9gr5id qc3s4z1d knj5qynh fo6rh5oj osnr6wyh hv4rvrfc dati1w0a p0x8y401 k4urcfbm iu8raji3 nfbje2wv']")
            print("cantidad de formularios a seleccionar {}".format(len(div_s)))

            Titular = "Venta Conjunto"
            # title = Titular + ds.iloc[iter][0] + " - intime"

            div_s[0].send_keys(ds.iloc[iter][0]) # insercion del titulo
            time.sleep(rd.randint(5.0, 6.0))

        # localizar el formulario precio y agregar.
            div_s[1].send_keys(str("1")) # insercion del precio
            time.sleep(rd.randint(5.0, 6.0))
        
        # localizar el formulario categoria y agregar
            div_category = self.driver.find_element_by_xpath("//div[@class='dati1w0a hv4rvrfc tr9rh885']")
            div_category.click()
            time.sleep(rd.randint(5.0, 6.0))
        
            try:

            # localizar la categoria correspondiente.
                div_cat = self.driver.find_elements_by_xpath("//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi abiwlrkh p8dawk7l']")
                div_cat[8].click() # por defecto la categoria sera 'ropa femenina y zapatos'
                time.sleep(rd.randint(5.0, 6.0))  
                pass

            except (exceptions.ElementNotInteractableException,
                    exceptions.NoSuchElementException):

                time.sleep(rd.randint(5.0, 6.0))
                cat_default = driver.find_element_by_xpath('//div[@class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl e72ty7fz qlfml3jp inkptoze qmr60zad abiwlrkh p8dawk7l p1ueia1e"]')
                cat_default.click()

            try:

                DIVS = driver.find_elements_by_xpath("//div[@class='discj3wi dati1w0a hv4rvrfc']")
                DIVS[2].click()
                time.sleep(rd.randint(5.0, 6.0))
                
            # Localizar el formulario de estado y agregar 
                list_state = self.driver.find_element_by_xpath("//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 opuu4ng7 oygrvhab kj2yoqh6 pybr56ya dflh9lhu f10w8fjw scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb']")
                list_state.click() # estado del producto (nuevo por defecto)
                time.sleep(rd.randint(5.0, 6.0))

            # Localizar el formulario de descripcion y agregar.
                DIVS[3].click()
                time.sleep(2.5)
                # desc_marc = "Marca intime "
                string_description = ds.iloc[iter][4] # + " Entrega a domicilio sin costo en toda la region metropolitana (consultar ubicacion) Envio a Regiones sin costo hasta $5000 montos superiores se descuentan los $5000"
                div_description = driver.find_elements_by_xpath(".//textarea[@class='oajrlxb2 rq0escxv f1sip0of hidtqoto lzcic4wl g5ia77u1 gcieejh5 bn081pho humdl8nn izx4hr6d oo9gr5id j83agx80 jagab5yi knj5qynh fo6rh5oj oud54xpy l9qdfxac ni8dbmo4 stjgntxs hv4rvrfc dati1w0a ieid39z1 k4urcfbm']")
                div_description[0].send_keys(string_description) # insercion de la descripcion del producto
                time.sleep(rd.randint(5.0, 6.0))
           
            # Localizar formulario del tamaño
                DIVS[5].click()
                time.sleep(rd.randint(4.0,5.0))

                size_div = driver.find_elements_by_xpath("//input[@class='oajrlxb2 rq0escxv f1sip0of hidtqoto e70eycc3 lzcic4wl g5ia77u1 gcieejh5 bn081pho humdl8nn izx4hr6d oo9gr5id qc3s4z1d knj5qynh fo6rh5oj osnr6wyh hv4rvrfc dati1w0a p0x8y401 k4urcfbm iu8raji3 nfbje2wv']")
                size_div[2].send_keys(ds.iloc[iter][2]) # insertar tamaño
                time.sleep(rd.randint(5.0, 6.0))

                #size_div[4].send_keys("Intime") # marca del producto
                #time.sleep(rd.randint(10.0, 11.0))

                #div_tag = driver.find_elements_by_xpath("//textarea[@class='oajrlxb2 rq0escxv f1sip0of hidtqoto lzcic4wl g5ia77u1 gcieejh5 bn081pho humdl8nn izx4hr6d oo9gr5id j83agx80 jagab5yi knj5qynh fo6rh5oj ni8dbmo4 stjgntxs sj5x9vvc ieid39z1 k4urcfbm']")
                #print(len(div_tag))
                #div_tag[0].send_keys(str(ds.iloc[iter][22])) # etiqueta de producto
                #time.sleep(rd.randint(2.0, 8.0))

            except (exceptions.NoSuchElementException, AttributeError, TypeError):

                print("no se seleciono estado\n")
                pass

            #Localizar publicar
            time.sleep(rd.randint(3.0, 4.0))
            div_next = driver.find_element_by_xpath("//div[@class='dati1w0a ihqw7lf3 hv4rvrfc discj3wi taijpn5t pfnyh3mw j83agx80 l6v480f0 bp9cbjyn']")
            if div_next:
                div_next.click()
                time.sleep(rd.randint(8.0, 10.0))
                try:
                    i = 0
                    groups_publishid = driver.find_element_by_xpath('//div[@class="n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3"]')
                    while True:
                        groups_publishid[i].click()
                        time.sleep(3)
                        i+=1
                        if i >= 19:
                            break
                        else:
                            continue
                        pass
                    pass
                except:
                    print("no se seleccionaron grupos")

                div_publicar = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu qypqp5cg']")
                div_publicar.click()
            else:
                # Localizar el objeto "Guardar Borrador"
                time.sleep(rd.randint(2.0, 3.0))
                div_save = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq g5ia77u1 tv7at329']")
                div_save.click() # Guardar Borrador.
                pass
            time.sleep(rd.randint(10.0, 11.0))
            try:
                Create_public = driver.find_element_by_xpath('//a[@aria-label="Crear publicación"]')
                Create_public.click()

            except:
                Create_public = driver.find_element_by_xpath('//a[@aria-label="Vender producto"]')
                Create_public.click()
                pass
            time.sleep(rd.randint(10.0, 11.0))
            _in = self.driver.find_element_by_xpath("//div[@class='bp9cbjyn rq0escxv j83agx80 cbu4d94t datstx6m taijpn5t tvx22r68 hv4rvrfc cifkjjtc dati1w0a oppkgyvt k1338c9a ntikgwu3 c34aag8n']")
            _in.click()
            time.sleep(rd.randint(10.0, 12.0))
            pass

        def CLOSE(self):
            driver.close()

#        divs[4].send_keys(str(ds.iloc[0][9])) # insercion de las etiquetas del producto
#        time.sleep(rd.randint(2.0, 7.0))
#        self.driver.find_element_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']").click() # pasar a siguiente para publicar


if __name__ == "__main__":

    YOUR_FACEBOOK_ID = input("Introduce usuario facebook: ")
    YOUR_FACEBOOK_PASSWD = input("Introduce contraseña facebook: ")
    publicar = publicfacebook(driver, 
            mail=YOUR_FACEBOOK_ID,
            passd=YOUR_FACEBOOK_PASSWD)
    publicar.intro_page()
    publicar.insert_details()
    publicar.CLOSE()
    pass

