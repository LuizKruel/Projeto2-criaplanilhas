"""
Projeto2-criaplanilhas
Descrição: módulo principal para manipular arquivos no formato xls.
Autora: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.1
"""

# importa pacotes (biblioteca padrão)

import random

# importa pacotes (terceiros)

from openpyxl import workbook

# importa pacotes (meus)

import manipula_xls

# manipula

def main():
    lista_planilhas = ['receitas','despesas', 'resultado']
    pasta = manipula_xls.cria_xls()
    pasta.active
    for planilha in lista_planilhas:
        manipula_xls.cria_planilha(planilha,pasta)
    pasta.save("orcamento.xls")
    
# execução do programa

if __name__== "__main__":
    main()
