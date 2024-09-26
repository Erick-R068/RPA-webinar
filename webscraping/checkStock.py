import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def check_stock(url):
    """
    Verifica el estado del stock de un producto en Amazon dada una URL.
    
    Parámetros:
    url (str): La URL del producto en Amazon.

    Retorna:
    str: Cantidad de stock disponible.
    """
    # Configuración de Chrome en modo Headless
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless=new")
    #chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--log-level=3")

    # Crear una instancia de Chrome
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navegar a la página de Amazon
        print("Ingresando a la URL...")
        time.sleep(0.5)
        driver.get(url)
        print("URL Ingresada!")

        # Esperar a que cargue el elemento del stock
        time.sleep(1)
        print("Esperando a que cargue el elemento...")
        stock_element = WebDriverWait(driver, 20).until(
            # Modificar según el criterio de busqueda del elemento:
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[5]/div/div[1]/div/div/button/span/span[4]"))
        )
        time.sleep(1)
        stock_status = stock_element.text.strip()  # Obtener el texto del elemento
        print(f"Estado del stock: {stock_status}")
        # Devolver el estado del stock
        return f"Stock disponible: {stock_status}"

    except TimeoutException as e:
        return f"Error: Elemento no encontrado (TimeoutException)"

    except Exception as e:
        return f"Error al obtener el estado del stock: {e}"

    finally:
        # Cerrar el navegador
        driver.quit()



# Ejemplo de uso de la función
if __name__ == "__main__":
    url = 'https://www.amazon.com/-/es/ProLiant-Computadora-servidor-empresarial-empresariales/dp/B07PW98RT5'
    stock_status = check_stock(url)
    print(f"Estado del stock: {stock_status}")


