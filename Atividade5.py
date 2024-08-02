# Função para calcular a comissão
def calcular_comissao(valor_produto, percentual_comissao):
    comissao = valor_produto * (percentual_comissao / 100)
    return comissao

# Solicita ao usuário o valor do produto
valor_produto = float(input("Digite o valor do produto (em reais): "))

# Solicita ao usuário o percentual da comissão
percentual_comissao = float(input("Digite o percentual de comissão (%): "))

# Calcula a comissão
comissao = calcular_comissao(valor_produto, percentual_comissao)

# Exibe o resultado
print(f"A comissão do vendedor é: R$ {comissao:.2f}")