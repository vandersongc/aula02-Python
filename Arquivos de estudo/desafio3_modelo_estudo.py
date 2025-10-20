'''
Desafio 3 – Simulador de Caixa Eletrônico
Peça um valor de saque. Use while para calcular quantas cédulas de 100, 50, 20 e 10 reais são necessárias. Exiba o detalhamento do saque.(Exemplo: “2 notas de 100, 1 nota de 50, 1 nota de 20…")
'''

# --- Desafio 3: Simulador de Caixa Eletrônico ---

print("--- Simulador de Caixa Eletrônico ---")
print("Notas disponíveis: R$ 100, R$ 50, R$ 20, R$ 10")
print("-" * 40)

# --- 1. Obter e Validar o Valor do Saque ---

# Usamos um loop 'while True' para garantir que o usuário
# digite um valor válido (número inteiro e múltiplo de 10)
while True:
    try:
        valor_saque = int(input("Digite o valor que deseja sacar: R$ "))
        
        # Validação 1: Não pode ser zero ou negativo
        if valor_saque <= 0:
            print("Valor inválido. Por favor, digite um valor positivo.")
        
        # Validação 2: Tem que ser múltiplo de 10 (pois 10 é nossa menor nota)
        elif valor_saque % 10 != 0:
            print("Valor inválido. Este caixa só pode sacar múltiplos de R$ 10.")
        
        # Se passou nas validações, quebra o loop
        else:
            break
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")

print("-" * 40)

valor_restante = valor_saque

# --- 2. Lógica do Cálculo (Usando WHILE) ---

# É bom guardar o valor original para mostrar no final
valor_restante = valor_saque

# Inicializamos os contadores de cada cédula
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0

# Este é o loop 'while' principal pedido no desafio.
# Ele vai rodar enquanto ainda houver dinheiro (valor_restante) para distribuir.
while valor_restante > 0:
    
    # Tentamos "pagar" com a maior nota primeiro
    if valor_restante >= 100:
        valor_restante -= 100  # Subtrai 100 do que falta pagar
        notas_100 += 1         # Adiciona 1 na contagem de notas de 100
    
    # Se não dá mais para pagar com 100, tenta com 50
    elif valor_restante >= 50:
        valor_restante -= 50
        notas_50 += 1
        
    # Se não dá com 50, tenta com 20
    elif valor_restante >= 20:
        valor_restante -= 20
        notas_20 += 1
        
    # Se não dá com 20, a única opção que resta é 10
    # (Lembre-se que já validamos que o valor é múltiplo de 10)
    elif valor_restante >= 10:
        valor_restante -= 10
        notas_10 += 1

# --- 3. Exibir o Detalhamento ---

print(f"Para sacar R$ {valor_saque:.2f}, você receberá:")

# Para ficar mais profissional, só mostramos as notas que 
# o usuário de fato vai receber (contagem > 0)
if notas_100 > 0:
    # Bônus: verifica se é singular ou plural
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

print("-" * 40)
print("Saque concluído com sucesso!")