import os
from termcolor import colored

erro = colored("OCORREU UM ERRO!", "red", attrs=["bold"])
lista = []

while True:
    opcao_escolhida = input("""Selecione uma opção: 
[i]nserir [a]pagar [l]istar:
""")

#Inserir item
    while opcao_escolhida == "i":
        inserirItem = input("Insira o valor, ou digite [s] para sair: ")
        lista.append(inserirItem)
        if inserirItem == "s":
            lista.pop() #Remover a letra S que foi inserida para sair do loop
            os.system("cls")
            break
        
#Listar itens
    if opcao_escolhida == "l":
        os.system("cls")
        for item in lista:
            index = lista.index(item)
            print(index, item.title())
            
#Deletar Item da lista 
    if opcao_escolhida == 'a':
        deletarItem = int(input("Digite o índice do objeto que você deseja deletar: "))
        try:
            del lista[deletarItem]
            os.system("cls")
            print("Item deletado. ")
        except:
            os.system("cls")
            print(erro, "O índice escolhido é inexistente. ")
            print("")
