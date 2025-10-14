# --- Desafio 1: Controle de Estoque ---

# 1. Peça ao usuário a quantidade inicial e valide a entrada
while True:
    try:
        # Tenta converter a entrada do usuário para um número inteiro
        estoque_atual = int(input("Digite a quantidade inicial de produtos em estoque: "))
        # Se a conversão for bem-sucedida, sai do loop de validação
        break
    except ValueError:
        # Se o usuário digitar algo que não seja um número, exibe um erro
        print("Erro: Por favor, digite um número inteiro válido.")

print(f"\nEstoque inicial definido: {estoque_atual} unidades.")
print("-----------------------------------------")

# 2. Loop principal para registrar vendas e reposições
while True:
    print("\nPara registrar uma VENDA, use um número negativo (ex: -10).")
    print("Para registrar uma REPOSIÇÃO, use um número positivo (ex: 20).")
    
    # Pede a próxima ação ao usuário e converte para minúsculas para facilitar a verificação
    entrada_usuario = input("Digite a operação ou 'sair' para finalizar: ").lower()

    # 3. Condição de parada do loop
    if entrada_usuario == 'sair':
        print("Finalizando o programa...")
        break  # Encerra o loop while

    # 4. Processa a entrada como uma operação de estoque
    try:
        # Tenta converter a entrada para um número inteiro
        quantidade_movimentada = int(entrada_usuario)

        # Verifica se é uma venda e se há estoque suficiente
        if quantidade_movimentada < 0 and (estoque_atual + quantidade_movimentada) < 0:
            print(f"Atenção: Venda de {abs(quantidade_movimentada)} unidades não permitida. Estoque insuficiente.")
        else:
            # Atualiza o valor do estoque
            estoque_atual += quantidade_movimentada
            if quantidade_movimentada < 0:
                print(f"✅ Venda de {abs(quantidade_movimentada)} unidades registrada.")
            elif quantidade_movimentada > 0:
                print(f"✅ Reposição de {quantidade_movimentada} unidades registrada.")
        
        # Mostra o saldo atualizado após cada operação válida
        print(f"--> Saldo atual: {estoque_atual} unidades.")

    except ValueError:
        # Se a entrada não for 'sair' nem um número, informa o usuário
        print("Erro: Entrada inválida. Digite um número ou 'sair'.")
    
    print("-----------------------------------------")

# 5. Exibe o saldo final de produtos
print("\n=========================================")
print(f"O saldo final de produtos em estoque é: {estoque_atual} unidades.")
print("=========================================")