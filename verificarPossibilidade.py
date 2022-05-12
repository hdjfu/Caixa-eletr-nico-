valor = input("Digite valor: ")
last = valor[-1] 	#salva qual o último digito de valor

valorInt = int(valor)

if last == "1" or last == "3":	#se ultimo digito 1 ou 3
	print("Não é possível sacar ", valorInt)
	print("Tente ", valorInt-1, "ou", valorInt+1) #sugerir dois valores diferentes
