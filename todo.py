import json

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
    
def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)


tarefas = carregar_tarefas()

def menu():
    print("""
    [1]Adicionar tarefa (texto simples)
    [2]Listar Tarefas
    [3]Remover Tarefa
    [0]Sair
    """)

def adicionar_tarefas(tarefas):
    adicionar = input("Informe suas tarefas: ")
    tarefas.append(adicionar)
    salvar_tarefas(tarefas)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Voce ainda nao adicionou nenhuma tarefa")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i} - {tarefa}")

def remover_tarefa(tarefas):
    if not tarefas:
        print("Voce ainda nao adicionou nenhuma tarefa")
    else: 
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i} - {tarefa}")
        num = int(input("Informe a numeracao do item que voce deseja remover: "))
        if num >= 1 and num <= len(tarefas):
            removido = tarefas.pop(num-1)
            salvar_tarefas(tarefas)
            print(f"esta tarefa foi removida: {removido}")
        else:
            print("digite um numero valido")

while True:
    
    menu()
    escolha = int(input("escolha umas das opcoes: "))
    
    if escolha == 1:
        adicionar_tarefas(tarefas)
    elif escolha == 2:
        listar_tarefas(tarefas)
    elif escolha == 3:
        remover_tarefa(tarefas)
    elif escolha == 0:
        break
    