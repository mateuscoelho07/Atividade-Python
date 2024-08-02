# Função para coletar e exibir informações do usuário
def exibir_informacoes():
    # Coletando informações do usuário
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    altura = input("Digite sua altura (em metros): ")
    peso = input("Digite seu peso (em kg): ")
    cidade = input("Digite sua cidade: ")
    
    # Exibindo as informações
    print("\nInformações do Usuário:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura} metros")
    print(f"Peso: {peso} kg")
    print(f"Cidade: {cidade}")

# Chamando a função para executar
exibir_informacoes()