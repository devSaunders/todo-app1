tarefas = []

def menu():
    print("""
    [1]Adicionar tarefa (texto simples)
    [2]Listar Tarefas
    [0]Sair
    """)

def adicionar_tarefas(tarefas):
    adicionar = input("Informe suas tarefas: ")
    tarefas.append(adicionar)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Voce ainda nao adicionou nenhuma tarefa")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i} - {tarefa}")

while True:
    
    menu()
    escolha = int(input("escolha umas das opcoes: "))
    
    if escolha == 1:
        adicionar_tarefas(tarefas)
    elif escolha == 2:
        listar_tarefas(tarefas)
    elif escolha == 0:
        break
    