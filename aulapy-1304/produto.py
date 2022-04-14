produto=input("Digite o nome do produto:  ") 
valor=int(input("Digite o valor da compra: "))

if valor <= 10:
    print("O valor da venda é",valor + valor * 70/100)
elif valor > 10 and valor <=30:
    print("O valor da venda ",valor + valor * 50/100)
elif valor >30 and valor <=50:
    print("O valor da venda é ",valor + valor * 40/100)    
elif valor >50:
    print("O valor da venda ",valor + valor * 30/100)
else:
    ("Print digite corretamente")    
    