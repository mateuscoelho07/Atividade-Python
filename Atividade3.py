# Taxa de câmbio fixa (1 USD = X EUR)
taxa_de_cambio = 0.91  # Exemplo: 1 USD = 0.91 EUR

# Função para converter dólares em euros
def converter_usd_para_eur(dolares):
    euros = dolares * taxa_de_cambio
    return euros

# Solicita ao usuário a quantidade em dólares
valor_usd = float(input("Digite o valor em dólares (USD): "))

# Realiza a conversão
valor_eur = converter_usd_para_eur(valor_usd)

# Exibe o resultado
print(f"{valor_usd} dólares (USD) equivalem a {valor_eur:.2f} euros (EUR)")