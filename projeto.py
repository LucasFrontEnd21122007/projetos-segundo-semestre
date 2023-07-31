# Classe para representar uma tarefa
class Tarefa:
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data

# Lista para armazenar as tarefas
lista_de_tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    data = input("Digite a data da tarefa (dd/mm/aaaa): ")
    nova_tarefa = Tarefa(descricao, data)
    lista_de_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para visualizar todas as tarefas
def visualizar_tarefas():
    if lista_de_tarefas:
        print("Lista de Tarefas:")
        for idx, tarefa in enumerate(lista_de_tarefas, 1):
            print(f"{idx}. Descrição: {tarefa.descricao} - Data: {tarefa.data}")
    else:
        print("Não há tarefas na lista.")

# Função para remover uma tarefa
def remover_tarefa():
    visualizar_tarefas()
    if lista_de_tarefas:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(lista_de_tarefas):
            tarefa_removida = lista_de_tarefas.pop(indice)
            print(f"Tarefa removida: {tarefa_removida.descricao}")
        else:
            print("Índice inválido.")
    else:
        print("Não há tarefas na lista.")

# Função principal do programa
def main():
    while True:
        print("\n----- Gerenciador de Tarefas -----")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Remover Tarefa")
        print("0. Sair")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            visualizar_tarefas()
        elif escolha == "3":
            remover_tarefa()
        elif escolha == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()