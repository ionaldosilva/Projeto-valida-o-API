import re
from validate_docbr import CPF



def cpf_valido(numero_do_cpf): 
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def telefone_valido(numero_celular):
        modelo = '([0-9]{2})9[0-9]{4}-[0-9]{4}'
        resposta= re.findall(modelo,numero_celular)
        return resposta

