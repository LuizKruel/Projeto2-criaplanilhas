"""
Projeto2-criaplanilhas
Descrição: módulo que oferece funções para manipular arquivos no formato xls.
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.1
"""

# importa pacotes

from openpyxl import workbook

# funções

def cria_xls()-> workbook:
    '''Esta função cria uma pasta de trabaho MS-Excel.'''
    pasta = workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: workbook)-> None:
    pasta.active
    pasta.create_sheet(nome_planilha)
