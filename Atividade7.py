# Frase fornecida
frase = "Ontem eu estava estudando Python."

# Palavra a ser buscada
palavra = "Python"

# Encontrar a posição da palavra
posicao = frase.find(palavra)

# Exibir o resultado
if posicao != -1:
    print(f"A palavra '{palavra}' está na posição {posicao}.")
else:
    print(f"A palavra '{palavra}' não foi encontrada na frase.")