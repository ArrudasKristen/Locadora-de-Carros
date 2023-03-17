# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:16:35 2023
@author: krist
"""

print('==================')
print('Bem vindo(a) à locadora Carros Lucena')
print('==================\n')

carros = [
    'Chevrolet Tracker - R$ 120/dia',
    'Chevrolet Onix - R$ 90/dia',
    'Chevrolet Spin - R$ 150/dia',
    'Hyundai HB20 - R$ 85/dia',
    'Hyundai Tucson - R$ 120/dia',
    'Fiat Uno - R$ 60/dia',
    'Fiat Mobi - R$ 70/dia',
    'Fiat Freemont - R$ 130/dia'
]

carroadquirido = [] 
res_princ = 0
while res_princ == 0:
    print('\nO que deseja fazer?')
    print('\n 0 - Mostrar Portfólio | 1 - Alugar um Carro | 2 - Devolver um Carro')
    res_acao = int(input())
    if res_acao == 0:
        for i, carro in enumerate(carros):
            print(f'{i} - {carro}')
        print('\n\n0 - CONTINUAR | 1 - SAIR')
        res_princ = int(input())
    elif res_acao == 1:
        for i, carro in enumerate(carros):
            print(f'{i} - {carro}')
        print('\nEscolha o código do carro:')
        res_carro = int(input())
        print('Deseja alugar por quantos dias?')
        res_dias = int(input())
        string = carros[res_carro]
        postraco = string.find(' -')
        posbarra = string.find('/')
        nomecarro = string[:postraco]
        valor = int(string[postraco+5:posbarra])
        print('\nVocê escolheu {} por {} dias.'.format(nomecarro, res_dias))
        print('O valor total do aluguel será de R$ {}. Deseja alugar? (0 - SIM | 1 - NÃO)'.format(valor*res_dias))
        res_confirma = int(input()) 
        if res_confirma == 0:
            carroadquirido.append(nomecarro)
            nomecarro = string
            print('\nO carro {} foi alugado com sucesso'.format(nomecarro))
            carros.pop(res_carro)
        print('\n\n0 - CONTINUAR | 1 - SAIR')
        res_princ = int(input())
    elif res_acao == 2:
        if carroadquirido:
            for i, carro in enumerate(carroadquirido):
                print(f'{i} - {carro}')
            print('\nInforme o carro a ser devolvido')
            res_devolvido = int(input())
            carros.append(nomecarro)
            print('\nVocê devolveu o carro {}'.format(carroadquirido[res_devolvido]))
            carroadquirido.pop(res_devolvido)
            print('\n\n0 - CONTINUAR | 1 - SAIR')
            res_princ = int(input())
        else:
            print('Não existem carros alugados ou todos foram devolvidos')
            print('\n\n0 - CONTINUAR | 1 - SAIR')
            res_princ = int(input())
