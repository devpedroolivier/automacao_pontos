import os
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright

# Carrega variáveis do .env
load_dotenv()

EMPREGADOR = os.getenv("TANGERINO_EMPREGADOR")
PIN = os.getenv("TANGERINO_PIN")
URL = "https://app.tangerino.com.br/Tangerino/pages/LoginPage"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        permissions=[]  # bloqueia câmera e microfone
    )
    page = context.new_page()
    page.goto(URL)

    # Clica em "Registrar Ponto"
    page.get_by_role("link", name="Registrar Ponto").click()

    # Preenche empregador e PIN
    page.get_by_role("textbox", name="Código do Empregador *").fill(EMPREGADOR)
    page.get_by_role("textbox", name="PIN *").fill(PIN)

    # Clica em registrar
    page.get_by_role("button", name="Registrar").click()

    # Fecha tudo
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
