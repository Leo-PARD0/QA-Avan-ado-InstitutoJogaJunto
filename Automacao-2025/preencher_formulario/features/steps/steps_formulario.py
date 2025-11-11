from behave import given, when, then #importa o behave

from selenium.webdriver import Edge # importa o Microsoft Edge
from selenium.webdriver.edge.options import Options # Importa as opções do edge
from selenium.webdriver.common.by import By # importa o Módulo By que interage com seletores html
from selenium.webdriver.support.ui import Select # Select lida com seletores de escolha
# from selenium.webdriver.common.keys import Keys  # keys não estava sendo usado então deixei comentado
import json # importa o json para poder buscar os dados
import os # importa os para buscar o caminho do arquivo json


import time

@given('que o navegador Microsoft Edge está aberto no site do joga junto')
def step_abrir_site(context):
    options=Options()
    options.add_argument("--Start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches",["enable-logging"])

    context.driver = Edge(options=options)
    print('logado')
    context.driver.get("https://formulario-contato-m8p8.onrender.com/")

    time.sleep(3)

@when('eu preencher o formulário')
def preencher_formulário(context):

    data_dir = os.path.join(os.path.dirname(__file__), 'dados.json')

    with open (data_dir, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    forms = {    
        'nome' : context.driver.find_element(By.NAME, "nome"),
        'email' : context.driver.find_element(By.NAME, "email"),
        'telefone' : context.driver.find_element(By.NAME, "telefone"),
        'cidade' : Select(context.driver.find_element(By.NAME, "cidade")),
        'bairro' : context.driver.find_element(By.NAME, "bairro"),
        'escolaridade' : context.driver.find_elements(By.NAME, "escolaridade"),
        'mensagem' : context.driver.find_element(By.NAME, "mensagem")
    }

    forms['nome'].send_keys(dados['nome'])
    forms['email'].send_keys(dados['email'])
    forms['telefone'].send_keys(dados['telefone'])
    forms['cidade'].select_by_visible_text(dados['cidade'])
    forms['bairro'].send_keys(dados['bairro'])

    for checkbox in forms['escolaridade']: # falta testar
        if checkbox.get_attribute("value") == dados['escolaridade']:
            checkbox.click()
            break


    #forms['escolaridade'][1].click()
    forms['mensagem'].send_keys(dados['mensagem'])
    time.sleep(3)

@then('eu enviarei a mensagem')
def enviar(context):
    enviar = context.driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary w-100 fw-bold"]')
    #enviar.click()

    input('Pressione enter...')
    time.sleep(3)