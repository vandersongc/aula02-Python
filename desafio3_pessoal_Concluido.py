'''
Desafio 3 – Simulador de Caixa Eletrônico
Peça um valor de saque. Use while para calcular quantas cédulas de 100, 50, 20 e 10 reais são necessárias. Exiba o detalhamento do saque.(Exemplo: “2 notas de 100, 1 nota de 50, 1 nota de 20…")
'''

print("--- Caixa Eletrônico ---")
print("Cédulas disponíveis: R$100, R$50, R$20 e R$10")
print("-" * 50)

while True:
    try:
        valor_saque = int(input("Digite o valor que deseja sacar: R$ "))
        
        if valor_saque <= 0:
            print('Valor de saque inválido. Digite um valor positivo.\n')
        elif valor_saque % 10 != 0:
            print('Valor de saque inválido. Digite um valor multiplo de 10.\n')
        else:
            break
        
    except ValueError:
        print('Valor inválido. Digite um valor inteiro.\n')

print("-" * 50)

valor_restante = valor_saque

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0

while valor_restante > 0:
    
    if valor_restante >= 100:
        valor_restante -= 100
        notas_100 += 1         

    elif valor_restante >= 50:
        valor_restante -= 50
        notas_50 += 1

    elif valor_restante >= 20:
        valor_restante -= 20
        notas_20 += 1

    elif valor_restante >= 10:
        valor_restante -= 10
        notas_10 += 1

print(f"Para sacar R$ {valor_saque:.2f}, você receberá:")

if notas_100 > 0:
    texto_plural = "notas" if notas_100 > 1 else "nota"
    print(f"- {notas_100} {texto_plural} de R$ 100")

if notas_50 > 0:
    texto_plural = "notas" if notas_50 > 1 else "nota"
    print(f"- {notas_50} {texto_plural} de R$ 50")

if notas_20 > 0:
    texto_plural = "notas" if notas_20 > 1 else "nota"
    print(f"- {notas_20} {texto_plural} de R$ 20")

if notas_10 > 0:
    texto_plural = "notas" if notas_10 > 1 else "nota"
    print(f"- {notas_10} {texto_plural} de R$ 10")

print("-" * 50)
print("Saque concluído com sucesso!")