import os



def limpatela():
    os.system("cls")
    input("Aperte enter para continuar...")

def exibeMenu():
    print('''
-------------------------------------
|            trab_motors            |
-------------------------------------
| entre com a opção desejada:       |
| 1 - Cadastrar novo Carro          |
| 2 - Buscar por placa              |
| 3 - Excluir por placa             |
| 4 - Listar carros                 |
| 5 - Sair                          |
-------------------------------------''')

def novoCarro():
    ''' TO DO: documentar
    '''
    carro = {"nome":'',"marca":'',"placa":'',"km":0}
    for atrib in carro:
        if atrib == 'km':
            carro[atrib] = int(input("Digite quilometragem do veículo: "))

            while carro[atrib] < 0:
                carro[atrib] = int(input("Digite quilometragem do veículo: "))

            #TO DO: validar kilometragem
  




    
        else:
            carro[atrib] = input(f"Digite {atrib} do veículo: ")
            
            while carro[atrib] == '':
                carro[atrib] = input(f"Digite {atrib} do veículo: ")
            

    print(f"Veículo inserido com sucesso!")
    input() #para poder exibir a mensagem

    return carro

#TO DO: escrever as funções de busca, remoção e printagem de listas

def buscar(listaCarros):
    '''
    #TO DO: documentar
    '''
    print("\n Lista de veículos e a placa: \n")
    for i in  range(len(listaCarros)):
        print("Carro: {} | Placa: {} ".format(listaCarros[i]['nome'],listaCarros[i]['placa']))
    
    print()
     
    
    plac = input("Digite nome da placa que você está buscado: ")
    a = 0
    for i in range(len(listaCarros)):
        if(plac == listaCarros[i]['placa']):
              print("Nome:{} || Marca: {} || Placa: {} || KM: {}".format(listaCarros[i]['nome'],listaCarros[i]['marca'],listaCarros[i]['placa'],listaCarros[i]['km']))
              a = a+1
    if(a <= 0):
        print("Placa inexistente no cadastro")  

    print()    
              
        
    input()

    #pass #TO DO: implementar

def excluir(listaCarros):
    '''
    #TO DO: documentar
    '''
    print("\n Lista de veículos e a placa: \n")
    for i in  range(len(listaCarros)):
        print("Carro: {} | Placa: {} ".format(listaCarros[i]['nome'],listaCarros[i]['placa']))
    
    print()
  
    
    plac = input("Digite nome da placa que você quer excluir ou Enter para sair: ")
    
    if (plac != ""):
        a =-1
        b =-1
        for i in range(len(listaCarros)):
            if(plac == listaCarros[i]['placa']):
                print("Nome:{} || Marca: {} || Placa: {} || KM: {}".format(listaCarros[i]['nome'],listaCarros[i]['marca'],listaCarros[i]['placa'],listaCarros[i]['km']))
                a = a+2
                b = i
                break
        if(b > -1):
            del (listaCarros[b])
            print("removido ...")
            for i in range(len(listaCarros)):
                if(plac == listaCarros[i]['placa']):
                    print("Nome:{} || Marca: {} || Placa: {} || KM: {}".format(listaCarros[i]['nome'],listaCarros[i]['marca'],listaCarros[i]['placa'],listaCarros[i]['km']))
                    input()
            
            excluir(listaCarros)
           
        if(a <= 0):
            print("Placa inexistente no cadastro")    
          
    
    input()
    return listaCarros
    #pass#TO DO: implementar



def imprimir(listaCarros):
    '''
    #TO DO: documentar
    '''
    for i in range(len(listaCarros)):
        print(f"\nVeículo {i+1}:")
        for campo in listaCarros[i]: #cada elemento da lista é um dicionário
            print(f"-->{campo}: {listaCarros[i][campo]}")

def listar(listaCarros):
    '''TO DO: documentar
    '''
    filtro = []
    #senão filtrar lista apenas com carros desejados e imprimir a lista filtrada
    imprimir(filtro)


