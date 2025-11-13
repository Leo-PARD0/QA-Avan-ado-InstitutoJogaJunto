from behave import given, when, then

from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os
import csv

import time

# https://lista.mercadolivre.com.br/notebook#D[A:notebook]

@given('que o usuário está no Microsoft Edge e acessou o Mercado Livre na página de notebooks')
def step_abrir_mercado_livre(context):
    options=Options()
    options.add_argument("--Start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches",["enable-logging"])

    context.driver = Edge(options=options)
    context.driver.get("https://lista.mercadolivre.com.br/notebook#D[A:notebook]")

    time.sleep(3)

@when('o usuário ordenar por menor preço')
def step_ordenar_menor_preco(context):
    ordem = context.driver.find_element(By.ID, ':Rlilie:-display-values')
    ordem.click()
    time.sleep(5)
    ordenar = context.driver.find_elements(By.CSS_SELECTOR, '[class="andes-list__item andes-list__item--size-medium"]')
    ordenar[0].click()
    time.sleep(6)
    minimo = context.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/aside/section/div[9]/ul/li[4]/form/div[1]/div/div/input')

    context.driver.execute_script("arguments[0].scrollIntoView();", minimo)

    minimo.send_keys('2000')
    minimo.send_keys(Keys.RETURN)
    time.sleep(5)
 



@when('listar os 5 notebooks mais baratos')
def step_listar_5_notebooks(context):
    resultados = context.driver.find_elements(By.CSS_SELECTOR, '[class="ui-search-layout__item"]')
    notebooks = [resultados[i] for i in range(5)]
    
    return notebooks, resultados

@then('o sistema retornará a opção mais barata')
def step_retornar_opcao_mais_barata(context):
    notebooks, resultados = step_listar_5_notebooks(context)
    for i in range(len(resultados)):
        titulo = resultados[i].find_element(By.CSS_SELECTOR, '[class="poly-component__title"]').text
        print(f"Título completo: {titulo}")
        preco = resultados[i].find_element(By.CSS_SELECTOR, '[aria-roledescription="Valor"]').text
        print(f"Preço: R$ {preco}")
        print(f"Notebook {i+1}: {titulo} - Preço: R$ {preco}")
        with open('notebooks_mais_baratos.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([titulo, preco])
        input('Pressione enter...')