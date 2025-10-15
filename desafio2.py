'''
Desafio 2 – Cálculo de Média de Temperaturas Semanais Peça as temperaturas de 7 dias usando for.Calcule e exiba:
a média da semana
a maior temperatura
a menor temperatura
'''
# Desafio 2 – Cálculo de Média de Temperaturas Semanais

# Inicializa uma lista vazia para armazenar as temperaturas
temperaturas = []
soma_temperaturas = 0.0

print("--- Média de Temperaturas da Semana ---")

# Pede as temperaturas de 7 dias usando um laço for
# O range(7) vai gerar números de 0 a 6, repetindo o bloco 7 vezes.
for dia in range(7):
  # Pede ao usuário para inserir a temperatura do dia
  # Usamos dia + 1 para mostrar "Dia 1", "Dia 2", etc.
  # float() converte o texto digitado para um número com casas decimais
  try:
    temp = float(input(f"Digite a temperatura do Dia {dia + 1}: "))
    
    # Adiciona a temperatura digitada na lista 'temperaturas'
    temperaturas.append(temp)
    
  except ValueError:
    print("Valor inválido. Por favor, digite apenas números.")
    # Caso o usuário não digite um número, podemos pedir para ele tentar de novo
    # Aqui, para simplificar, vamos atribuir 0 e continuar.
    temperaturas.append(0.0)


# Verifica se a lista não está vazia para evitar erro de divisão por zero
if temperaturas:
  # a) Calcula a média da semana
  # sum(temperaturas) soma todos os itens da lista
  # len(temperaturas) conta quantos itens existem na lista
  media_semanal = sum(temperaturas) / len(temperaturas)

  # b) Encontra a maior temperatura
  maior_temperatura = max(temperaturas)

  # c) Encontra a menor temperatura
  menor_temperatura = min(temperaturas)

  # Exibe os resultados formatados
  print("\n--- Resultados ---")
  print(f"A média de temperatura da semana foi: {media_semanal:.2f}°C")
  print(f"A maior temperatura registrada foi: {maior_temperatura}°C")
  print(f"A menor temperatura registrada foi: {menor_temperatura}°C")
else:
  print("Nenhuma temperatura foi registrada para calcular os resultados.")


