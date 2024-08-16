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
        driver.get("https://alejo20788.github.io/PaginaPruebas/")

        # Llama a la función de prueba
        test_id_and_name(driver)

    finally:
        # Cierra el navegador
        driver.quit()

def test_id_and_name(driver):
    """
    Prueba la presencia de elementos por ID y NAME.
    """
    # Busca el elemento por ID
    elemento = driver.find_element(By.ID, "noImportante")
    if elemento:
        print("El elemento por ID fue encontrado")

def testName(driver):
    # Busca el elemento por NAME
    elemento2 = driver.driver.find_element(By.NAME, "ultimo")
    if elemento2:
        print("El elemento por NAME fue encontrado")

if __name__ == "__main__":
    main()
