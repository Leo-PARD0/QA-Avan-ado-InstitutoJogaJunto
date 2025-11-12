from behave import given, when, then #importa o behave

from selenium.webdriver import Edge # importa o Microsoft Edge
from selenium.webdriver.edge.options import Options # Importa a classe options que permite alterar as opções do edge
from selenium.webdriver.common.by import By # importa o Módulo By que interage com seletores html
from selenium.webdriver.support.ui import Select # Select lida com seletores de escolha
# from selenium.webdriver.common.keys import Keys  # keys não estava sendo usado então deixei comentado
import json # importa o json para poder buscar os dados
import os # importa os para buscar o caminho do arquivo json

import time # importa time para pedir para o código esperar

@given('que o navegador Microsoft Edge está aberto no site do joga junto')
def step_abrir_site(context):
    options=Options() # a variável options receberá as opções do navgegador
    options.add_argument("--Start-maximized") # ad argument passa a instrução de maximizar
    options.add_argument("--disable-blink-features=AutomationControlled") # add argument passa a instrução de desabilitar a notificação de controle por automação
    options.add_experimental_option("excludeSwitches",["enable-logging"]) # ad experimental option passa a instrução de excluir as mensagens desnecessárias do log

    context.driver = Edge(options=options) # context.driver receberá todas as opções de options
    print('logado')
    context.driver.get("https://formulario-contato-m8p8.onrender.com/") # pesquisará o site do formulário

    time.sleep(3) # espera o site carregar

@when('eu preencher o formulário')
def preencher_formulário(context):

    data_dir = os.path.join(os.path.dirname(__file__), 'dados.json') # encontra o caminho dos dados e salva na variável

    with open (data_dir, 'r', encoding='utf-8') as arquivo: # abre dados.json como arquivo
        dados = json.load(arquivo) # salva o json como dicionário

    forms = {    # dicionário com os seletores do formulário
        'nome' : context.driver.find_element(By.NAME, "nome"),
        'email' : context.driver.find_element(By.NAME, "email"),
        'telefone' : context.driver.find_element(By.NAME, "telefone"),
        'cidade' : Select(context.driver.find_element(By.NAME, "cidade")),
        'bairro' : context.driver.find_element(By.NAME, "bairro"),
        'escolaridade' : context.driver.find_elements(By.NAME, "escolaridade"), # escolaridade recebe "send_keys" no lugar de key pois tem mais de um dado, com isso ele se torna uma lista de valores
        'mensagem' : context.driver.find_element(By.NAME, "mensagem")
    }

    for chave, elemento in forms.items(): # loop para preencher o fórmulário. A escolha do loop veio do fato de muitos campos do formulário terem a mesman lógica de preenchimento, então podemos conter elas no loop para simplificar o código. Chave será a chave dentro dos 2 dicionários, elemento se refere ao valor de forms.
        valor = dados[chave] # a variável valor se refere ao valor do dicionário dados
        
        if chave == 'cidade': # verificador da ação que será executada
            elemento.select_by_visible_text(valor)
        elif chave == 'escolaridade':
            for checkbox in elemento:
                if checkbox.get_attribute("value") == valor:
                    checkbox.click()
                    break
        else:
            elemento.send_keys(valor)

    time.sleep(3)

@then('eu enviarei a mensagem')
def enviar(context):
    enviar = context.driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary w-100 fw-bold"]')
    enviar.click()

    input('Pressione enter...')
    time.sleep(3)