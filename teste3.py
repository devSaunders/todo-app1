import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo) #isso o json pegar a lista, converter para ,json e escrever ela no arquivo

def carregar_tarefas():
    try: #isso faz o programa tentar abrir o arquivo para leitura
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo) 
    except: #caso nao tenha nada na lista ele retorna ela vazia
        return []

tarefas = carregar_tarefas()

def ler_int(mensagem): #isso faz uma validacao na hora em que o aplicativo pede um numero. caso seja str o programa nao quebra e sim pede um numero valido para o usuario
    while True:
        valor = input(mensagem)
        try:
            convert = int(valor)
            return convert
        except ValueError:
            print("digite um numero valido")


def menu(): 
    print("""
[1]Adicionar tarefa
[2]Ver Tarefas
[3]Marcar tarefas como concluida
[4]sair
""")

def adicionar_tarefa(tarefas):
    tarefa = input("Qual a sua tarefa de hoje? ")
    tarefa = {
        "tarefas": tarefa,
        "concluido": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas) #isso salva oq esta acontecendo no arquivo json

def listar_tarefas(tarefas):
    if not tarefas:
        print("voce ainda nao tem nenhuma tarefa")
        return
    for i, tarefa in enumerate(tarefas, start=1): #isso enumera as tarefas para deixar mais bonito
        if tarefa["concluido"]:
            status = "[X]"
        else:
            status = "[ ]"
        print(f"{i} tarefa: {tarefa['tarefas']} - {status}")

def marcar_concluida(tarefas):
    if not tarefas:
        print("voce ainda nao tem nenhuma tarefa")
        return
    listar_tarefas(tarefas)
    valor = ler_int("informe o numero da tarefa que voce deseja marcar como concluida: ")
    while valor < 1 or valor > len(tarefas):
        print("voce digitou um numero invalido")
        valor = ler_int("informe o numero da tarefa que voce deseja marcar como concluida: ")
    indice = valor - 1
    tarefas[indice]["concluido"] = True
    print(f"A {tarefas[indice]['tarefas']} foi marcada como concluida!")
    salvar_tarefas(tarefas) #isso salva oq esta acontecendo no arquivo json

while True:
    menu()
    
    escolha = ler_int("Informe oq deseja fazer: ")

    if escolha == 1:
        adicionar_tarefa(tarefas)
    elif escolha == 2:
        listar_tarefas(tarefas)
    elif escolha == 3:
        marcar_concluida(tarefas)
    elif escolha == 4:
        break
