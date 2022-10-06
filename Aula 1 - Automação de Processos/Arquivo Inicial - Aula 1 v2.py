# passo 1: Entrar no sistema da empresa
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyperclip.copy('Google Chrome')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)

# pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
while not pyautogui.locateOnScreen('drive.png', confidence=0.9):
    time.sleep(1)

# passo 2: Navegar no sistema e encontrar a base de vendas
time.sleep(5)
pyautogui.click(x=351, y=267)
pyautogui.click(clicks=2)

# passo 3: Fazer o download da base de vendas
while not pyautogui.locateOnScreen('sheet.png', confidence=0.9):
    time.sleep(1)
time.sleep(2)
pyautogui.click(x=380, y=266)  # clicar no arquivo
time.sleep(2)
pyautogui.click(x=1161, y=169)  # clicar nos 3 pontinhos
pyautogui.click(x=938, y=579)  # clicar para fazer download
time.sleep(5)  # esperar o download acabar

# passo 4: Importar a base de vendas para o Python
import pandas as pd

tabelaImportada = pd.read_excel(r'C:\Users\br_ed\Downloads\Vendas - Dez.xlsx')  # o 'r' antes do caminho do arquivo
# transoforma o texto do caminho em um texto "cru", sem considerar possiveis comandos da linguagem
print(tabelaImportada)

# passo 5: Calcular os indicadores da empresa
faturamento = tabelaImportada['Valor Final'].sum()
print(f'Total = R${faturamento:,.2f}')
quantidade = tabelaImportada['Quantidade'].sum()
print(f'Quantidade de produtos = {quantidade:,}')
time.sleep(2)

# passo 6: Enviar um email para a diretoria com os indicadores de venda
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
while not pyautogui.locateOnScreen('gmail.png', confidence=0.9):
    time.sleep(1)
time.sleep(2)
pyautogui.click(x=146, y=179)
while not pyautogui.locateOnScreen('botao-enviar.png', confidence=0.9):
    time.sleep(1)
time.sleep(5)
pyautogui.write('edu.sp.cs@gmail.com')
# pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')  # seleciona o email

pyautogui.press('tab')  # pula para o campo assunto
pyperclip.copy('Relatório de Vendas (Teste de automação com Python)')
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('tab')  # pula para o corpo do email
textoEmail = f'''
Prezados,

Segue Relatório das Vendas:
Faturamento = R${faturamento:,.2f}
Quantidade de produtos = {quantidade:,}

Fico à disposição.
'''
pyperclip.copy(textoEmail)
pyautogui.hotkey('ctrl', 'v')

# passo 7: anexar arquivo no email
pyautogui.click(x=325, y=678)
time.sleep(2)
pyperclip.copy(r'C:\Users\br_ed\Downloads\Vendas - Dez.xlsx')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(4)

pyautogui.click(x=208, y=681)  # enviar

# fim
pyautogui.alert('Fim da automação!')
