import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

def buscar_dominio(DOMINIO):
    web = f"https://www.nic.cu/dom_det.php?domsrch={DOMINIO}"

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    
    print("[i] Obteniendo información...")
    
    with webdriver.Firefox(service=Service(executable_path="geckodriver.exe"), options=options) as driver:  
        driver.get(web)
        
        print("\n", driver.title)

        print("\n===Información general del Dominio===")
        dominio = driver.find_element(By.XPATH,'/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text
        print("Dominio: ", dominio)
        
        organizacion = driver.find_element(By.XPATH,'/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text
        print("Organización: ", organizacion)
        
        direccion = driver.find_element(By.XPATH,'/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[4]/td[2]/table/tbody/tr/td[2]').text
        print("Dirección :", direccion)
        
        print("\n===DNS Primario===")
        dns_nombre = driver.find_element(By.XPATH, '/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text
        print("Nombre: ", dns_nombre)
        
        ip = driver.find_element(By.XPATH, '/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text
        print("Dirección IP: ", ip)
        
        print("\n===Contacto Administrativo===")
        cont_nombre = driver.find_element(By.XPATH, '/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text
        print("Nombre: ", cont_nombre)
        
        cont_organizacion = driver.find_element(By.XPATH, '/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text
        print("Organización: ", cont_organizacion)
        
        cont_direccion = driver.find_element(By.XPATH, '/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]').text
        print("Dirección: ", cont_direccion)
        
        cont_telefono = driver.find_element(By.XPATH, '/html/body/center/div[1]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr/td[2]').text
        print("Teléfono: ", cont_telefono)
          
        print("\n==> Con datos de: ", driver.current_url)
        
if __name__ == "__main__":
    
    arg = sys.argv    
    buscar_dominio(arg[1])
