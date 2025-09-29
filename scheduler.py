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

# Lista de dias da semana e horários desejados
dias_da_semana = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
horarios = ['06:00', '11:00', '12:00', '15:00']

# Agendar a tarefa para cada dia e horário
for dia in dias_da_semana:
    for horario in horarios:
        # Acessa a função de agendamento dinamicamente
        getattr(schedule.every(), dia).at(horario).do(job)

print("✅ Scheduler iniciado. Tarefas agendadas de segunda a sexta...")

while True:
    schedule.run_pending()
    time.sleep(30)  # Checa a cada 30 segundos