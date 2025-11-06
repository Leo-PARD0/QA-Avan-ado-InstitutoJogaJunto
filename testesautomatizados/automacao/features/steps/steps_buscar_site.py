from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager as EdgeDriver 
""" python -m pip install --upgrade selenium webdriver-manager """
from selenium.webdriver.edge.service import service as EdgeService
import time
from behave import given, when, then

# Step 1

@given('Dado que o navegador esteja na página inicial')
def step_open_browser(context):
    options= webdriver.EdgeOptions()
    options.add_argument('--start-maximized')

    context.driver = webdriver.Edge(
        service=EdgeService(EdgeDriver().install()),
        options=options
    )
    context.driver.get("https://www.google.com")
    time.sleep(3)
