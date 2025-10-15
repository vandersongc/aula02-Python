'''
Desafio 3 – Simulador de Caixa Eletrônico
Peça um valor de saque. Use while para calcular quantas cédulas de 100, 50, 20 e 10 reais são necessárias. Exiba o detalhamento do saque.(Exemplo: “2 notas de 100, 1 nota de 50, 1 nota de 20…")
'''

# Desafio 3 – Simulador de Caixa Eletrônico

print("--- Caixa Eletrônico ---")
print("Cédulas disponíveis: R$100, R$50, R$20 e R$10")

# Pede um valor de saque e converte para inteiro
try:
  valor_saque = int(input("Digite o valor que deseja sacar: R$ "))
except ValueError:
  print("Entrada inválida. Por favor, digite um número inteiro.")
  valor_saque = -1 # Define um valor inválido para encerrar o programa


# Mantém uma cópia do valor original para exibir no final
valor_original = valor_saque 
resto = valor_saque

# Variáveis para contar a quantidade de cada cédula
cedulas_100 = 0
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0

# A lógica principal é feita com um laço 'while'
# O laço continuará enquanto ainda houver algum valor a ser distribuído
while resto > 0:
  if resto >= 100:
    cedulas_100 = resto // 100  # Pega a parte inteira da divisão
    resto %= 100                # O resto da divisão por 100 continua no laço
  elif resto >= 50:
    cedulas_50 = resto // 50
    resto %= 50
  elif resto >= 20:
    cedulas_20 = resto // 20
    resto %= 20
  elif resto >= 10:
    cedulas_10 = resto // 10
    resto %= 10
  else:
    # Se o resto for menor que 10, o valor não é válido para saque
    print(f"\nNão é possível sacar o valor de R${valor_original}.")
    print("Este caixa trabalha apenas com notas de R$100, R$50, R$20 e R$10.")
    # Zera as contagens para não exibir o detalhamento
    cedulas_100 = cedulas_50 = cedulas_20 = cedulas_10 = 0
    break # Encerra o laço 'while'

# Exibe o detalhamento do saque, apenas para as notas que serão entregues
# Verifica se o saque foi bem-sucedido (se o valor original era válido)
if valor_original > 0 and resto == 0:
  print(f"\n--- Detalhamento do Saque de R${valor_original} ---")
  if cedulas_100 > 0:
    # Operador ternário para escrever "nota" ou "notas" corretamente
    texto_nota = "nota" if cedulas_100 == 1 else "notas" 
    print(f"{cedulas_100} {texto_nota} de R$100")
  if cedulas_50 > 0:
    texto_nota = "nota" if cedulas_50 == 1 else "notas"
    print(f"{cedulas_50} {texto_nota} de R$50")
  if cedulas_20 > 0:
    texto_nota = "nota" if cedulas_20 == 1 else "notas"
    print(f"{cedulas_20} {texto_nota} de R$20")
  if cedulas_10 > 0:
    texto_nota = "nota" if cedulas_10 == 1 else "notas"
    print(f"{cedulas_10} {texto_nota} de R$10")