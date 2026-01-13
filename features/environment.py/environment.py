from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Executa UMA vez antes de tudo
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

def after_all(context):
    # Executa UMA vez depois de tudo (fecha o navegador)
    if context.driver:
        context.driver.quit()