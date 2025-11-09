# ============================================================
# 🧩 Importação das bibliotecas necessárias 1️⃣2️⃣3️⃣
# ============================================================

from behave import given, when, then

from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# ============================================================
# 🧠 Definição dos passos do teste BDD (Gherkin)
# ============================================================

# ----------------------------------------
# 1️⃣ Etapa "DADO QUE..."
# ----------------------------------------
@given('que o usuário está com o micronsoft edge aberto')
def step_open_browser(context):
    options=Options()
    options.add_argument("--Start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches",["enable-logging"])

    context.driver = Edge(options=options)
    context.driver.get("https://www.google.com")

    time.sleep(3)

@given('com a página do whatsapp aberta')
def step_abrir_WhatsApp(context):
    campo = context.driver.find_element(By.NAME, "q")

    campo.send_keys("WhatsApp Web")
    campo.send_keys(Keys.RETURN)

    time.sleep(4)

    resultados = context.driver.find_elements(By.CSS_SELECTOR, "h3")
    
    if resultados:
        resultados[0].click()

        time.sleep(5)

        assert "web.whatsapp" in context.driver.current_url.lower()

        print("🌐 Site do WhatsApp Web aberto com sucesso!")
    else:
        raise AssertionError("❌ Nenhum resultado encontrado.")
    
# ----------------------------------------
# 2️⃣ Etapa "QUANDO..."
# ----------------------------------------
@when('o usuário Logar')
def step_wait_forLogin(context):
    time.sleep(60)
    
    grid = context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Lista de conversas"]')

    if grid:
        print('🌐 Login detectado com sucesso!')
    else:
        raise AssertionError("❌ Timeout: login não detectado.")

@when('encontrar o grupo de mensagem')
def step_encontrar_grupo(context):
    pesquisa = context.driver.find_element(By.CSS_SELECTOR, '[contenteditable="true"]')

    pesquisa.send_keys('[QA IBTECH | AGO/25]')
    pesquisa.send_keys(Keys.RETURN)

    conversa = context.driver.find_elements(By.CSS_SELECTOR, '[role="row"]')
    if conversa:
        conversa[0].click()

        time.sleep(3)

        print('Conversa aberta')
    else:
        AssertionError(("❌ conversa não encontrada."))

# ----------------------------------------
# 3️⃣ Etapa "ENTÃO..."
# ----------------------------------------

@then('a mensagem será editada e enviada')
def step_send_mensage(context):
    escrever = context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Digitar no grupo [QA IBTECH | AGO/25]"]') # [aria-label="Digitar na conversa com _____"]

    escrever.send_keys('Estou enviando mais uma mensagem por automação.')
    escrever.send_keys(Keys.RETURN)
    escrever.send_keys('Vou tirar um print usando: context.driver.save_screenshot("evidence_qr.png") pra deixar de evidência')
    escrever.send_keys(Keys.RETURN)

    """  
    for i in range(5):
        mensagem = i+1
        escrever.send_keys(str(mensagem))
        escrever.send_keys(Keys.RETURN) 
    """
    
    time.sleep(3)

    context.driver.save_screenshot("evidence_qr.png")

    escrever.send_keys('Quem tiver difículdade pode me mandar mensagem')

    time.sleep(3)

    print('mensagem enviada com sucesso, código desligando')