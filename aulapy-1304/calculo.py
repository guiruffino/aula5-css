print('Bem vindo a calculadora')
modulo=int(input("\tDigite 1 para DIVIDIR\n \t Digite 2 para MULTIPLICAR\n \t Digite 3 para SOMAR\n \t Digite 4 para SUBTRAIR \n \t Digite: "))
numero1=float(input("Digite o valor do primeiro numero:  "))
numero2=float(input("Digite o valor do segundo numero:  "))
if modulo >=1 and modulo <=4 :   
    if modulo==1:
        print("Foi selecionado Divisao\n O valor calculado é: ",numero1/numero2)        
    elif modulo==2:
        print("Foi selecionado Multiplicacao\n O valor calculado é: ",numero1*numero2)
    elif modulo==3:
        print("Foi selecionado Soma\n O valor calculado é: ",numero1+numero2)
    elif modulo==4:
        print("Foi selecionado Subtração\n O valor calculado é ",numero1-numero2)
    else:
        print("Digite a função corretamente")
else:
    print("Digitee a função corretamente")