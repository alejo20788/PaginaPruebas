"""
Este módulo realiza pruebas básicas de elementos en una página web utilizando Selenium.

Se conecta a un navegador Edge, abre una página web específica, busca elementos por ID y NAME, 
e imprime mensajes si los elementos son encontrados. Finalmente, cierra el navegador.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

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
        elemento = driver.find_element(By.ID, "noImportante")
        if elemento:
            print("El elemento by ID fue encontrado")

        # Busca el elemento por NAME
        elemento2 = driver.find_element(By.NAME, "ultimo")
        if elemento2:
            print("El elemento by NAME fue encontrado")

    finally:
        # Cierra el navegador
        driver.quit()

if __name__ == "__main__":
    main()
