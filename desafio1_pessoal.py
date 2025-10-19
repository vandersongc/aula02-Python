'''
Desafio 1- Peça ao usuário a quantidade inicial de produtos em estoque. Use while para permitir registrar vendas e reposições até o usuário digitar “sair”. Ao final, exiba o saldo de produtos.
'''

print('Controle de Estoque')

while True:
    try:
        est_inicial = int(input('Digite o estoque atual: '))
        break
    except ValueError:
        print('\nVocê digitou um valor não válido.\n')

est_atual = int(est_inicial)

while True:

    print('\nPara vendas utilize um valor negativo: exemplo: (-10 )')
    print('Para reposição utilize um valor positivo: exemplo: (10 )\n')

    inp_usuario = input('Digite o valor de: \nVenda; \nreposição, ou \n Sair: ').lower()

    if inp_usuario == sair:
        print('Processo encerrado.')
        break
   