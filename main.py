import logging
import time
from playwright.sync_api import Playwright, sync_playwright

EMPREGADOR = "X20B2"
PIN = "1295"
URL = "https://app.tangerino.com.br/Tangerino/pages/LoginPage"

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("tangerino.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def run(playwright: Playwright) -> None:
    logging.info("Iniciando automação do Tangerino...")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        permissions=[]  # bloqueia câmera e microfone
    )
    page = context.new_page()

    logging.info("Acessando página de login...")
    page.goto(URL)

    logging.info("Clicando em 'Registrar Ponto'...")
    page.get_by_role("link", name="Registrar Ponto").click()

    # Adiciona uma espera explícita para o campo de entrada do empregador
    # Isso garante que a página carregou completamente o campo antes de tentar preenchê-lo
    # evitando o erro de Timeout.
    logging.info("Aguardando o campo de empregador carregar...")
    page.wait_for_selector('role=textbox[name="Código do Empregador *"]')

    logging.info("Preenchendo código do empregador...")
    page.get_by_role("textbox", name="Código do Empregador *").fill(EMPREGADOR)

    logging.info("Preenchendo PIN...")
    page.get_by_role("textbox", name="PIN *").fill(PIN)

    logging.info("Clicando em 'Registrar'...")
    page.get_by_role("button", name="Registrar").click()

    # Espera fixa antes de encerrar (5 segundos, ajustável)
    logging.info("⏳ Aguardando 5 segundos para garantir registro...")
    time.sleep(5)

    context.close()
    browser.close()
    logging.info("Automação finalizada.")

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
