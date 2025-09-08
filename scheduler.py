import schedule
import time
import subprocess
import sys
from pathlib import Path

# Caminho absoluto para main.py
PROJECT_DIR = Path(__file__).parent
SCRIPT = PROJECT_DIR / "main.py"

def job():
    print("▶️ Executando automação do Tangerino...")
    subprocess.run([sys.executable, str(SCRIPT)])

# Horários desejados
schedule.every().day.at("05:00").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("15:00").do(job)

print("✅ Scheduler iniciado. Aguardando horários definidos...")

while True:
    schedule.run_pending()
    time.sleep(30)  # checa a cada 30 segundos
