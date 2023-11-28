import pyautogui
import time
from datetime import datetime

# FUNCAO DE HORARIO E DATA
def obter_mensagem():
    # Obtém a data e horário atual
    data_e_hora_atual = datetime.now()

    # Define a data desejada para as férias (15 de dezembro de 2023)
    data_ferias = datetime(2023, 12, 15, 0, 0, 0)

    # Calcula a diferença entre as datas
    diferenca = data_ferias - data_e_hora_atual

    # Extrai os componentes de tempo
    dias = diferenca.days
    horas, resto = divmod(diferenca.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    # Determina a saudação com base no horário atual
    if 6 <= data_e_hora_atual.hour < 12:
        saudacao = "Bom dia"
    elif 12 <= data_e_hora_atual.hour < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    # Mensagem personalizada para as férias
    mensagem = f"{saudacao}, CLT safada! Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para as suas tao sonhadas ferias!"

    return mensagem

# 2 - Abrir o whatsapp!
pyautogui.click(374, 1060, duration=2) 
pyautogui.click(168, 64, duration=2)  # Clica no campo de texto
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')    
time.sleep(10)  # espera 10s para poder esperar as conversas

# # 3 - Abrir a conversa
pyautogui.click(309, 292, duration=1)  # abre a primeira conversa
pyautogui.click(807, 985, duration=1)  # abre o chat

# # Obter a mensagem
mensagem = obter_mensagem()

# # Digitar a mensagem no chat
pyautogui.write(mensagem)
pyautogui.press('enter')  # Pressiona Enter para enviar a mensagem

# # Aguardar um momento para garantir que a mensagem foi enviada antes de prosseguir
time.sleep(2)

# Caminho do arquivo MP3
caminho_audio = 'D:\\2. Faculdade ADS\\0.PYTHON\\projetos\\automacao-bom-dia\\audio\\'   #caminho do audio 
pyautogui.click(235,1064, duration=2) #abre os arquivos
pyautogui.click(908,260, duration=2) #abre o caminho 
pyautogui.press('backspace')
time.sleep(1)
pyautogui.write(caminho_audio) #cola o caminho
time.sleep(1)
pyautogui.press('enter') 
# pyautogui.click(776,378, duration=2) #clica na musica

# Definir as coordenadas iniciais
x_inicial, y_inicial = 776, 378

# Definir as coordenadas finais (destino)
x_final, y_final = 807, 985

# Definir as coordenadas iniciais
x_inicial, y_inicial = 776, 378

# Definir as coordenadas finais (destino)
x_final, y_final = 807, 985

# Simular clique e arrastar
pyautogui.moveTo(x_inicial, y_inicial)
pyautogui.mouseDown()  # Pressiona o botão do mouse (inicia o clique)

# # Aguarda um curto período de tempo (pode ajustar conforme necessário)
# time.sleep(1)

pyautogui.dragTo(x_final, y_final, duration=2)  # Arrasta para as coordenadas finais
pyautogui.mouseUp()  # Libera o botão do mouse (encerra o clique)
time.sleep(5)
pyautogui.press('enter')