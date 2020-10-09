import rotinas
import os

lst_veiculos = [] #lista inicia vazia

while True:
    rotinas.exibeMenu()
    op = int(input("Digite a opção desejada:"))
    while(op <1 or op >5):
        op =  int(input("Digite a opção desejada:"))

    if(op==1): 
        
        

        carro = rotinas.novoCarro(lst_veiculos)
        lst_veiculos.append(carro)
        rotinas.limpatela()
    elif(op==2):
       
       buscarV = rotinas.buscar(lst_veiculos)
       rotinas.limpatela()

        #TO DO: Passar a lista de veículos e a placa
        # Se a placa existir, imprimir a informação do veículo
        # senão informar placa inexistente no cadastro
        
        
    elif(op==3):
        #TO DO: Passar a lista de veículos e a placa
        # Se a placa existir, excluir veículo
        # senão informar placa inexistente no cadastro

        excluir = rotinas.excluir(lst_veiculos)
        lst_veiculos = excluir
        rotinas.limpatela()
    elif(op==4):
        #TO DO: função deve perguntar se o usuário quer listar todos, por marca ou por kilometragem
        # Se por marca, imprimir apenas os que possuem a marca entrada pelo usuário
        # Se por quilometragem imprimir apenas os veículos que possuam km menor que a digitada pelo usuário
        rotinas.listar(lst_veiculos)
        input()
        rotinas.limpatela()
    else:
        #encerrar programa
        rotinas.limpatela()
        exit()
    




