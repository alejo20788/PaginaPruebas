"""
Este módulo realiza pruebas básicas de elementos en una página web utilizando Selenium.

Se conecta a un navegador Edge, abre una página web específica, 
busca elementos por ID, NAME, CLASS_NAME, LINK_TEXT y PARTIAL_LINK_TEXT,
e imprime mensajes si los elementos son encontrados. Finalmente, cierra el navegador.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def main():
    """
    Función principal para realizar pruebas en la página web.
    """
    # Inicializa el controlador del navegador Edge
    driver = webdriver.Edge()

    try:
        # Abre la página web
        driver.get("http://www.clouditeducation.com/pruebas")

        # Busca el elemento por ID
        try:
            elemento_id = driver.find_element(By.ID, "noImportante")
            if elemento_id:
                print("El elemento by ID fue encontrado")
        except NoSuchElementException:
            print("No se encontró el elemento por ID")

        # Busca el elemento por NAME
        try:
            elemento_name = driver.find_element(By.NAME, "ultimo")
            if elemento_name:
                print("El elemento by NAME fue encontrado")
        except NoSuchElementException:
            print("No se encontró el elemento por NAME")

        # Busca el elemento por CLASS_NAME
        try:
            elemento_class = driver.find_element(By.CLASS_NAME, "rojo")
            if elemento_class:
                print("El elemento by CLASS_NAME fue encontrado")
        except NoSuchElementException:
            print("No se encontró el elemento por CLASS_NAME")

        # Busca el elemento por LINK_TEXT
        try:
            elemento_link = driver.find_element(By.LINK_TEXT, "Pagina 2")
            if elemento_link:
                print("El elemento by LINK_TEXT fue encontrado")
        except NoSuchElementException:
            print("No se encontró el elemento por LINK_TEXT")

        # Busca el elemento por PARTIAL_LINK_TEXT
        try:
            elemento_partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Link")
            if elemento_partial_link:
                print("El elemento by PARTIAL_LINK_TEXT fue encontrado")
        except NoSuchElementException:
            print("No se encontró el elemento por PARTIAL_LINK_TEXT")

    finally:
        # Cierra el navegador
        driver.quit()

if __name__ == "__main__":
    main()
