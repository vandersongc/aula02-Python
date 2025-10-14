'''
Desafio 1- Peça ao usuário a quantidade inicial de produtos em estoque. Use while para permitir registrar vendas e reposições até o usuário digitar “sair”. Ao final, exiba o saldo de produtos.
'''
tentativas = 2
produto = input('Digite o nome do produto: ')
estoque = int(input('Digite o saldo atual do estoque: '))
venda = int(input('Quantidade vendida: '))
estoque_atual = estoque - venda
estoque_min = 30
estoque_max = 90

while tentativas > 0:
    if estoque_atual < estoque_min:
        print(f'Necessidade de resposição')
        reposicao = estoque_max -estoque_atual





'''
Desafio 2 – Cálculo de Média de Temperaturas Semanais Peça as temperaturas de 7 dias usando for.Calcule e exiba:
a média da semana
a maior temperatura
a menor temperatura
'''




'''
Desafio 3 – Simulador de Caixa Eletrônico
Peça um valor de saque. Use while para calcular quantas cédulas de 100, 50, 20 e 10 reais são necessárias. Exiba o detalhamento do saque.(Exemplo: “2 notas de 100, 1 nota de 50, 1 nota de 20…")
'''

