print("<<<            LANCHONETE DA ESQUINA              >>>")
print("                 C A R D Á P I O                     ")
print("-----------------------------------------------------")
print("|  Código     |Produto             |Preço Unitário  |")
print("-----------------------------------------------------")
print("|   100       |Cachorro Quente     |R$ 3,70         |")
print("|   101       |Bauru Simples       |R$ 4,30         |")
print("|   102       |Bauru com Ovo       |R$ 4,80         |")
print("|   103       |Hamburguer          |R$ 5,70         |")
print("|   104       |Cheeseburguer       |R$ 4,50         |")
print("|   105       |Misto quente        |R$ 2,50         |")
print("-----------------------------------------------------")
codigo = int(input("Código ...: "))
quant = int(input("Quantidade: "))
print("-----------------------------------------------------")
print("       <<<PEDIDO>>>       ")
print("\n")

if codigo == 100:
    print("Cachorro Quente: ",quant, " x ","R$ 3,70")
    valor = 3.70*quant
    print("-----------------------------------------------------")
    print(f">>>>>>> Total à Pagar: R$ {valor:.2f}")
    print("-----------------------------------------------------")
    print("<<< Agradecemos a preferência! Bom apetite! >>>")
elif codigo == 101:
    print("Bauru Simples: ",quant, " x ","R$ 4,30")
    valor = 4.30*quant
    print("-----------------------------------------------------")
    print(f">>>>>>> Total à Pagar: R$ {valor:.2f}")
    print("-----------------------------------------------------")
    print("<<< Agradecemos a preferência! Bom apetite! >>>")
elif codigo == 102:
    print("Bauru com Ovo: ",quant, " x ","R$ 4,80")
    valor = 4.80*quant
    print("-----------------------------------------------------")
    print(f">>>>>>> Total à Pagar: R$ {valor:.2f}")
    print("-----------------------------------------------------")
    print("<<< Agradecemos a preferência! Bom apetite! >>>")
elif codigo == 103:
    print("Hamburguer: ",quant, " x ","R$ 5,70")
    valor = 5.70*quant
    print("-----------------------------------------------------")
    print(f">>>>>>> Total à Pagar: R$ {valor:.2f}")
    print("-----------------------------------------------------")
    print("<<< Agradecemos a preferência! Bom apetite! >>>")
elif codigo == 104:
    print("Cheeseburguer: ",quant, " x ","R$ 4,50")
    valor = 4.50*quant
    print("-----------------------------------------------------")
    print(f">>>>>>> Total à Pagar: R$ {valor:.2f}")
    print("-----------------------------------------------------")
    print("<<< Agradecemos a preferência! Bom apetite! >>>")
elif codigo == 105:
    print("Misto quente: ",quant, " x ","R$ 2,50")
    valor = 2.50*quant
    print("-----------------------------------------------------")
    print(f">>>>>>> Total à Pagar: R$ {valor:.2f}")
    print("-----------------------------------------------------")
    print("<<< Agradecemos a preferência! Bom apetite! >>>")
else:
    print("Código Inexistente")




