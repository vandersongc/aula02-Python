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

    print('\nPara vendas utilize um valor negativo: exemplo: (-10 ).')
    print('Para reposição utilize um valor positivo: exemplo: (10 ).\n')
    print('Para encerrar o processo digite SAIR.\n')

    print(f'Seu estoque atual é: {est_atual}')
    inp_usuario = input('Digite o algum dos comandos acima citados: ').lower()

    if inp_usuario ==  'sair':
        print('Processo encerrado.')
        break

    try:

        quant_mov = int(inp_usuario)

        if quant_mov > est_atual or quant_mov == 0:
            print('\nQuantidade movimentada superior ao estoque ou valor de movimentação nulo.')
        
        else:
            est_mov = est_atual + quant_mov
            print(f'Estoque ({est_atual}) + Movimentação do estoque ({quant_mov}) = Novo Pós movimentação ({est_mov}) ')
            est_atual = est_mov
    except ValueError:
        print("Valor não válido.")