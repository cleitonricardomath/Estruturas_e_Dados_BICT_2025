# -*- coding: utf-8 -*-

# Passo 1: Função para exibir o menu de opções
def exibir_menu():
    """
    Esta função imprime as opções disponíveis para o usuário.
    Não recebe parâmetros e não retorna nada.
    """
    print("\n--- Agenda Telefônica ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Consultar Contato")
    print("4. Listar Todos os Contatos")
    print("5. Sair")
    print("-------------------------")

# Passo 2: Função para adicionar um contato à agenda
def adicionar_contato(agenda):
    """
    Solicita ao usuário o nome e o telefone do novo contato
    e o adiciona ao dicionário 'agenda'.

    Parâmetros:
    agenda (dict): O dicionário que armazena os contatos.
                   As chaves são os nomes e os valores são os telefones.
    """
    nome = input("Digite o nome do contato: ")
    # Verifica se o contato já existe
    if nome in agenda:
        print(f"'{nome}' já existe na agenda. Deseja atualizá-lo? (s/n)")
        resposta = input().lower()
        if resposta != 's':
            print("Operação cancelada.")
            return # Sai da função se o usuário não quiser atualizar

    telefone = input(f"Digite o telefone de {nome}: ")
    agenda[nome] = telefone  # Adiciona ou atualiza o contato no dicionário
    print(f"Contato '{nome}' adicionado/atualizado com sucesso!")

# Passo 3: Função para remover um contato da agenda
def remover_contato(agenda):
    """
    Solicita ao usuário o nome do contato a ser removido
    e o remove do dicionário 'agenda', se existir.

    Parâmetros:
    agenda (dict): O dicionário que armazena os contatos.
    """
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in agenda:
        del agenda[nome]  # Remove o contato do dicionário
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

# Passo 4: Função para consultar um contato na agenda
def consultar_contato(agenda):
    """
    Solicita ao usuário o nome do contato a ser consultado
    e exibe seu telefone, se existir.

    Parâmetros:
    agenda (dict): O dicionário que armazena os contatos.
    """
    nome = input("Digite o nome do contato que deseja consultar: ")
    if nome in agenda:
        print(f"Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

# Passo 5: Função para listar todos os contatos da agenda
def listar_contatos(agenda):
    """
    Exibe todos os contatos (nome e telefone) presentes na agenda.

    Parâmetros:
    agenda (dict): O dicionário que armazena os contatos.
    """
    if not agenda:  # Verifica se o dicionário está vazio
        print("A agenda está vazia.")
        return

    print("\n--- Lista de Contatos ---")
    # Itera sobre os itens (pares chave-valor) do dicionário
    for nome, telefone in agenda.items():
        print(f"Nome: {nome}, Telefone: {telefone}")
    print("-------------------------")

# Passo 6: Função principal que executa a agenda telefônica
def main():
    """
    Função principal que gerencia o loop do programa e
    as interações com o usuário.
    """
    # Inicializa a agenda como um dicionário vazio.
    # O dicionário é a estrutura de dados que usaremos para armazenar
    # os contatos, onde o nome do contato será a chave e o número
    # de telefone será o valor.
    agenda_telefonica = {}

    # Loop principal do programa
    while True:
        exibir_menu()  # Mostra as opções para o usuário
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            print("\n--- Adicionar Contato ---")
            adicionar_contato(agenda_telefonica)
        elif escolha == '2':
            print("\n--- Remover Contato ---")
            remover_contato(agenda_telefonica)
        elif escolha == '3':
            print("\n--- Consultar Contato ---")
            consultar_contato(agenda_telefonica)
        elif escolha == '4':
            listar_contatos(agenda_telefonica)
        elif escolha == '5':
            print("Saindo da agenda telefônica. Até logo!")
            break  # Encerra o loop e o programa
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")

# Passo 7: Executar a função principal quando o script é rodado
# A construção 'if __name__ == "__main__":' garante que a função 'main()'
# só será chamada quando o script for executado diretamente (e não quando
# for importado como um módulo em outro script).
if __name__ == "__main__":
    main()
