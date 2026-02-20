import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo) #isso o json pegar a lista, converter para ,json e escrever ela no arquivo

def carregar_tarefas():
    try: #isso faz o programa tentar abrir o arquivo para leitura
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo) 
    except: #caso nao tenha nada na lista ele retorna ela vazia
        return FileNotFoundError

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
[3]Alternar concluida (marcar/desmarcar)
[4]Excluir tarefa
[5]Editar tarefa
[6]Sair
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

def excluir_tarefa(tarefas):
    if not tarefas:
        print("voce ainda nao tem nenhuma tarefa")
        return
    listar_tarefas(tarefas)
    valor = ler_int("informe qual das tarefas voce deseja remover: ")
    while valor < 1 or valor > len(tarefas): #isso verifica se o usuario informou uma tarefa existente
        print("essa tarefa nao existe")
        valor = ler_int("informe uma tarefas valida: ")
    indice = valor - 1
    removida = tarefas.pop(indice) #isso remove a tarefa 
    print(f"A tarefa {removida['tarefas']} foi removida!")
    salvar_tarefas(tarefas) #isso salva oq esta acontecendo no arquivo json

def alternar_concluida(tarefas):
    if not tarefas:
        print("voce ainda nao tem nenhuma tarefa")
        return
    listar_tarefas(tarefas)
    valor = ler_int("informe a tarefa que voce deseja alterar: ")
    while valor < 1 or valor > len(tarefas):
        print("essa tarefa nao existe")
        valor = ler_int("informe uma tarefa valida: ")
    indice = valor - 1
    tarefas[indice]["concluido"] = not tarefas[indice]["concluido"]
    print(f"agora a tarefa {tarefas[indice]['tarefas']} foi alterada")
    salvar_tarefas(tarefas)

def editar_tarefas(tarefas):
    if not tarefas:
        print("voce ainda nao tem nenhuma tarefa")
        return
    listar_tarefas(tarefas)
    valor = ler_int("informe a tarefa que voce deseja editar: ")
    while valor < 1 or valor > len(tarefas):
        print("essa tarefa nao existe")
        valor = ler_int("informe uma tarefa valida: ")
    indice = valor - 1
    editar = input("informe o novo texto: ")
    tarefas[indice]["tarefas"] = editar
    print("Tarefa editada com sucesso")
    salvar_tarefas(tarefas)

while True:
    menu()
    
    escolha = ler_int("Informe oq deseja fazer: ")

    if escolha == 1:
        adicionar_tarefa(tarefas)
    elif escolha == 2:
        listar_tarefas(tarefas)
    elif escolha == 3:
        alternar_concluida(tarefas)
    elif escolha == 4:
        excluir_tarefa(tarefas)
    elif escolha == 5:
        editar_tarefas(tarefas)
    elif escolha == 6:
        break
