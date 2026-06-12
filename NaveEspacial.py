## Definindo as variáveis
combustivel = 100
tripulantes = []

## Definindo as funções

def viajar():  ### Viajar irá gastar o combústivel

    global combustivel  ### Avisa a função que vamos modificar uma variável externa
    if len(tripulantes) == 0:
        print("Não há tripulantes na na nave, adicione um tripulante!")
        print("Para adicionar um tripulante selecione 4")

    else:
        if combustivel>=30:
            combustivel = combustivel - 30
            print("* A nave está pronta para a viagem")

        else:
            print("* Combustível insuficiente para a viagem, abasteça!")
    travarMenu()


def abastecer():
    global combustivel
    combustivel = 100
    print("* Tanque cheio⛽")
    travarMenu()
def status_nave():
    print(f"-------- STATUS da NAVE -----------")
    print(f"* Temos {combustivel} de combustível")
    print(f"* Os tripulantes são {tripulantes}")
    travarMenu()
# Registrando novo tripulante
def registrarTripulante():
    novoTripulante = input("Inserir novo tripulante : ")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com sucesso!🚀")
    travarMenu()

##Criando uma função que tira o ultimo tripulante
def tirandotripulante():
    global tripulantes
    if len(tripulantes) == 0:
        print("Lista vazia, adicione um tripulante!")
        registrarTripulante()
    else:
        print(f"Os tripulantes são: {tripulantes}")
    tripulantes.pop()
    travarMenu()
## Criando uma função para pausar o código entre as interações do usuário

def travarMenu():
    ##o código começa aqui
    input("\nPressione <ENTER> para continuar....")


## Criando um menu

while True: ## esse loop roda para sempre
    print("\nBem Vindo ao menu interativo da nave. Por favor selecione uma opção:")
    print("\n1 - Mostrar status da nave | 2 - viajar | 3 - Abastecer | 4 - Novo Tripulante | 5 - Remover Tripulante | 6 - Sair")
    opcao = input("Escolha:")


## chamando funções
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulante()
    elif (opcao == "5"):
        tirandotripulante()
    elif (opcao == "6"):
        print("Viagem encerrada")
        break
