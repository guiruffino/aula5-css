idade=int(input("Digite a idade: "))

if idade>=18 and idade <=65:
    print("Eleitor Obrigatorio")
elif idade >=16 and idade <=18 and idade>65:
    print("Eleitor facultativo")
elif idade >65:
    print("Eleitor facultativo")    
else:
    print("Nao eleitor")    
