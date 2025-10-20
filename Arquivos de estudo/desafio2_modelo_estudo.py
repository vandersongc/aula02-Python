'''
Desafio 2 – Cálculo de Média de Temperaturas Semanais Peça as temperaturas de 7 dias usando for.Calcule e exiba:
a média da semana
a maior temperatura
a menor temperatura
'''
# --- Desafio 2: Média de Temperaturas Semanais ---

print("Bem-vindo ao Cálculo de Temperaturas da Semana!")
print("Por favor, insira a temperatura de cada um dos 7 dias.")

# 1. Criamos uma lista vazia para guardar as temperaturas
temperaturas = []

# 2. Usamos um loop 'for' para pedir as 7 temperaturas
# O range(7) vai gerar números de 0 a 6 (total de 7 repetições)
for i in range(7):
    # Usamos um loop 'while True' para garantir que o usuário digite um NÚMERO
    while True:
        try:
            # Pedimos a temperatura. Usamos 'i + 1' para mostrar "Dia 1", "Dia 2", etc.
            temp_dia = float(input(f"Digite a temperatura do Dia {i + 1}: "))
            
            # 3. Adicionamos a temperatura válida à nossa lista
            temperaturas.append(temp_dia)
            
            # Se a conversão para float deu certo, podemos sair do 'while True'
            break 
            
        except ValueError:
            # Se o usuário digitou um texto (ex: "trinta"), o float() dará um erro.
            # O 'except' captura esse erro e pede para digitar novamente.
            print("Entrada inválida. Por favor, digite apenas números (ex: 25.5).")

print("-" * 30) # Imprime uma linha para separar

# --- Cálculos ---

# a) Média da semana
# sum() soma todos os itens da lista
# len() conta quantos itens existem na lista (sabemos que é 7)
media_semana = sum(temperaturas) / len(temperaturas)

# b) Maior temperatura
# A função max() encontra o maior valor na lista
maior_temp = max(temperaturas)

# c) Menor temperatura
# A função min() encontra o menor valor na lista
menor_temp = min(temperaturas)

# --- Exibição dos Resultados ---

print(f"Temperaturas registradas: {temperaturas}")
print(f"a) Média da semana: {media_semana:.2f}°C") # .2f formata para 2 casas decimais
print(f"b) Maior temperatura: {maior_temp}°C")
print(f"c) Menor temperatura: {menor_temp}°C")