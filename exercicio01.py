#TarefaClassRoom 04/02/2023

#Variáveis
n1=float(input("Entre com n1: "))
n2=float(input("Entre com n2: "))
n3=float(input("Entre com n3: "))
me=float(input("Entre com ME: "))

#Fórmula
ma = ((n1 + n2*2 + n3*3 + me)/7)
print ("A média de aproveitamento é: ", ma)

if ma >=6:
 print ("Aprovado")
else:
 print ("Reprovado")