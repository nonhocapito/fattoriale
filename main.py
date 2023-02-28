#versione brutta----------------------------------------------------------------
def fattoriale(numero):
	if numero==0:
		fattoriale=1
	else:
		fattoriale=numero
		for i in range(1, numero, 1):		#(start=1, stop=n, step=1)
			fattoriale=fattoriale*(numero-i)
		
	return fattoriale

#versione bella-----------------------------------------------------------------
def fact(number):
	result=1
	for i in range(1, number+1):
		result*=i
	return result

#script-------------------------------------------------------------------------
cond=True
while cond==True:
	n=int(input("Inserire numero: "))
	print(f"{n}! = "+str(fattoriale(n)))
	print(f"{n}! = "+str(fact(n)))
	print(80*"-"+"\n")
