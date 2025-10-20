'''
Desafio 2 – Cálculo de Média de Temperaturas Semanais Peça as temperaturas de 7 dias usando for.Calcule e exiba:
a média da semana
a maior temperatura
a menor temperatura
'''

print("Bem-vindo ao Cálculo de Temperaturas da Semana!")
print("Por favor, insira a temperatura de cada um dos 7 dias.\n")

temperatura = []

for i in range (7):

    while True:
        try:
            temp_dia = float(input(f'Digite a temperatura do dia {i+1}: '))

            temperatura.append(temp_dia)

            break

        except ValueError:

            print("Entrada inválida. Por favor, digite apenas números (ex: 25.5).")

print("-" * 50)

media_semanal = sum(temperatura)/len(temperatura)
max_temp = max(temperatura)
min_temp = min(temperatura)

print(f"Temperaturas registradas: {temperatura}")
print(f"a) Média da semana: {media_semanal:.2f}°C") 
print(f"b) Maior temperatura: {max_temp}°C")
print(f"c) Menor temperatura: {min_temp}°C\n")

    



