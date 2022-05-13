
#Número de notas dentro do caixa
n200 = 100
n100 = 100
n50 = 100
n20 = 100
n10 = 100
n5  = 100
n2  = 100

#Número de notas entregues
e200 = 0
e100 = 0
e50 = 0
e20 = 0
e10 = 0
e5  = 0
e2  = 0

saque = int(input("Digite o valor a ser retirado: "))

#Entregar notas de 200
while saque >= 200:
    
    n200 = n200 - 1      #Diminui em 1 a quantidade de notas de 200 do caixa
    e200 = e200 + 1     #Adiciona em 1 a quantidade de notas de 200 entregues
    saque = saque - 200 #Subtrai 200 do valor do saque


while saque >= 100:
    
    n100 = n100- 1
    e100 = e100 + 1
    saque = saque - 100



while saque >= 50:
    
    n50 = n50 - 1       
    e50 = e50 + 1       
    saque = saque - 50  


while saque >= 20:
    
    n20 = n20- 1
    e20 = e20 + 1
    saque = saque - 20

while saque >= 10:
    
    n10 = n10- 1
    e10 = e10 + 1
    saque = saque - 10

while saque >= 5:
    
    n5 = n5- 1
    e5 = e5 + 1
    saque = saque - 5

while saque >= 2:
    
    n2 = n2- 1
    e2 = e2 + 1
    saque = saque - 2
print("----------------------")
print("Notas entregues:")
print("200", e200)
print("100", e100)
print("50: ", e50)
print("20: ", e20)
print("10: ", e10)
print("5 : ", e5)
print("2 : ", e2)
print("\nNotas restantes:")
print("200", e200)
print("100", e100)
print('50:', n50)
print('20:', n20)
print('10:', n10)
print("5 :", n5)
print('2 :', n2)
print("----------------------")
