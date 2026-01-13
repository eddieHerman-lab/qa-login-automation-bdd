from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Mapeamento de Elementos (Design Pattern Simples)
INPUT_USER = (By.ID, "user-name")
INPUT_PASS = (By.ID, "password")
BTN_LOGIN  = (By.ID, "login-button")
MSG_ERRO   = (By.CSS_SELECTOR, "[data-test='error']")

@given('que estou na página de login do "{url}"')
def abrir_pagina(context, url):
    # O driver já vem configurado do environment.py
    context.driver.get(url)

@when('preencho o campo de usuário com "{usuario}"')
def preencher_usuario(context, usuario):
    context.driver.find_element(*INPUT_USER).send_keys(usuario)

@when('preencho o campo de senha com "{senha}"')
def preencher_senha(context, senha):
    context.driver.find_element(*INPUT_PASS).send_keys(senha)

@when('clico no botão de entrar')
def clicar_login(context):
    context.driver.find_element(*BTN_LOGIN).click()
    time.sleep(1) # Pausa didática

@then('devo ser redirecionado para a vitrine de produtos')
def validar_login_sucesso(context):
    assert "inventory.html" in context.driver.current_url, "Falha: Não entrou na página de inventário"

@then('devo visualizar a mensagem de erro "{mensagem_esperada}"')
def validar_erro(context, mensagem_esperada):
    elemento_erro = context.driver.find_element(*MSG_ERRO)
    texto_atual = elemento_erro.text
    assert mensagem_esperada in texto_atual, f"Erro esperado: {mensagem_esperada}, Obtido: {texto_atual}"