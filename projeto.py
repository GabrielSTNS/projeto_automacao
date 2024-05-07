# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time

pyautogui.PAUSE = 0.3 # esperar 0.3 segundos entre cada ação feita pelo pyautogui

# abrindo o navegador Edge com o pyautogui
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
# time.sleep(1) # esperar 1 segundo para aplicar o click do mouse
pyautogui.click(x=414, y=55)

# entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# fazer login na plataforma
pyautogui.click(x=505, y=352)
pyautogui.write('gabriel2000.santana@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345')
pyautogui.press('tab')
pyautogui.press('enter')

# importando a biblioteca pandas e renomeando como "pd"
import pandas as pd

tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, 'codigo']

    # clicar no campo de código
    pyautogui.click(x=524, y=245)

    # preencher o campo
    pyautogui.write(str(codigo))
    
    # passar para o proximo campo
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    # tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # preco
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # obs
    pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')

    # clicar no botao de cadastrar
    pyautogui.press('enter')
    pyautogui.scroll(5000)