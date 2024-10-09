from phonenumbers import PhoneNumberFormat, parse as phone_parse, format_number as phone_format
import pandas as pd
import os

root_directory = os.getcwd()
excel_name = 'telefones.xlsx'

def colunas_corretas(df: pd.DataFrame) -> bool:
    colunas_esperadas = ['telefone', 'msg enviada', 'mensagem']

    if list(df.columns) == colunas_esperadas:
        return True
    else:
        return False


def create_excel() -> None:
    df = pd.DataFrame({
        'telefone': '',
        'msg enviada': '',
        'mensagem': ''
    }, index=[0])

    df.to_excel(root_directory + '\\' + excel_name, index=False)


def excel_vazio(df_phones: pd.DataFrame) -> bool:
    if len(df_phones) > 0:
        return False
    
    return True


def excel_exists(excel_directory: str) -> bool:
    if os.path.exists(excel_directory):
        return True
    
    return False


def format_number_phone(phone: str) -> str:
    tel = phone_format(phone_parse(str(phone), 'BR'), PhoneNumberFormat.E164)
    return tel


def remove_duplicates_numbers(df_phones: pd.DataFrame) -> pd.DataFrame:
    df_without_duplicates = df_phones.drop_duplicates(subset=['telefone'])
    return df_without_duplicates


def phones_to_send_msg(df_phones: pd.DataFrame) -> list:
    df_phones = df_phones[df_phones['msg enviada'].isna()]

    return df_phones['telefone'].dropna().tolist()


def confirm_msg_sent(df_phones: pd.DataFrame, phone: str, msg_sent='SIM') -> None:
    df_phones.loc[df_phones['telefone'] == phone, 'msg enviada'] = msg_sent

    df_phones.to_excel(root_directory + '\\' + excel_name, index=False)