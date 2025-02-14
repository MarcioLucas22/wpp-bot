import os
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import urllib
import utils
import traceback
import warnings


warnings.filterwarnings("ignore")

if not utils.excel_exists(utils.root_directory + '\\' + utils.excel_name):
    print('Excel "telefones.xlsx" não existe. Criando um novo...')
    utils.create_excel()
    print('Excel criado com sucesso!')
    print('Gentileza preenchê-lo com as informações necessárias para dar continuidade.')
    time.sleep(10)
    os._exit(0)


df_phones = pd.read_excel(utils.root_directory + '\\' + utils.excel_name)

if not utils.colunas_corretas(df_phones):
    print('Colunas do Excel não estão com o nome correto...')
    print('Gentileza alterar o nome e deixar exatamente da seguinte forma: phone, msg_enviada, mensagem')
    time.sleep(15)
    os._exit(0)


if utils.excel_vazio(df_phones):
    print('Excel encontra-se vazio. Gentileza preenchê-lo para dar continuidade...')
    time.sleep(10)
    os._exit(0)

df_phones = pd.read_excel(utils.root_directory + '\\' + utils.excel_name)
df_phones = utils.remove_duplicates_numbers(df_phones)

for i in range(3):
    try:
        phones = utils.phones_to_send_msg(df_phones)
        if len(phones) > 0:
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('log-level=3')

            driver = webdriver.Chrome(options=chrome_options)

            driver.get(f"https://web.whatsapp.com/")

            while len(driver.find_elements(By.ID, 'side')) < 1:
                time.sleep(1)

            for i, phone in enumerate(phones):
                message = df_phones.loc[i, 'mensagem']
                msg_formatted = urllib.parse.quote(message)
                
                phone_formatted = utils.format_number_phone(phone)
                if len(phone_formatted) == 14:
                    link = f'https://web.whatsapp.com/send?phone={phone_formatted}&text={msg_formatted}'
                    driver.get(link)                    

                    while len(driver.find_elements(By.XPATH, "//button[@aria-label='Enviar'] | //*[text()='OK']")) < 1:
                        time.sleep(1)

                    if len(driver.find_elements(By.XPATH, "//button[@aria-label='Enviar']")):
                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar']"))).click()
                        utils.confirm_msg_sent(df_phones, phone)
                    else:
                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='OK']"))).click()
                        utils.confirm_msg_sent(df_phones, phone, 'Número inválido')
                else:
                    utils.confirm_msg_sent(df_phones, phone, 'Número inválido')

                time.sleep(3)

            driver.close()
            print('\nTodas as mensagens enviadas com sucesso!\n')
            time.sleep(10)
            break
        else:
            print('Nenhum telefone para enviar mensagem.')
            time.sleep(10)
            break        
    except Exception:
        error = traceback.format_exc()
        driver.close()
        print('Ocorreu um erro: ', error)
        print('\nRecomeçando em 5 segundos caso ainda tenha telefones para enviar mensagem...')
        time.sleep(5)

os._exit(0)
