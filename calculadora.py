import time
import sys
def cal(i):
   for c in i:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(2./70)
def lin(u):
   for c in u+'\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(3./100)
def io(a):
	for c in a:
	    sys.stdout.write(c)
	    sys.stdout.flush()
	    time.sleep(1./300)
lin('--------------------')
user = input("Usuario:")
def longuitud():
	try:
		radi=float(input('Radio\n>>>'))
		pi = 3.14159
		valor = 2*pi*radi
		print (valor)
	except ValueError:
		cal("Error 01")
def sumar():
	try:
		a = int(input("Sumar\n>>>"))
		b = int(input("Con\n>>>"))
		valor = a+b
		print (a,"+",b,"=",valor)
	except ValueError:
		cal("Error 02\n")
def hm():
	try:
		a=int(input("Multiplica del >"))
		i=int(input("Hasta el >"))
		i+=1
		print(a) 
		for c in range(a,i):
			print (a*c)
	except ValueError:
		cal("Error 03\n")
def concatenar():
	try:
		c=str(input("Concatenar\n>>>"))
		d=str(input("Con\n>>>"))
		resultado = c+d
		print("Resultado: "+resultado)
	except:
		cal("Error 04\n")
def restar():
	try:
		x = int(input("Restar\n>>>"))
		y = int(input("Con\n>>>"))
		resultado = x-y
		print(x,"-",y,"=",resultado)
	except ValueError:
		cal("Error 05\n")
def dividir():
	try:
		x = int(input("Dividir\n>>>"))
		y = int(input("Entre\n>>>"))
		resultado = x/y
		print("Resultado:",resultado)
	except ValueError:
		cal('Error 06\n')
	except ZeroDivisionError:
		cal('Error 08\n')
def multiplicar():
	try:
		o = int(input("Multiplica\n>>>"))
		b = int(input("Por\n>>>"))
		value = o*b
		print(o,"x",b,"=",value)
	except ValueError:
		cal("Error 07\n")
x=True
while x:
	button = input(f"{user}:")
	if button == 'exit':
		cal("Saliendo...\n")
		x=False
	elif button == 'help':
		cal("------------------\n")
		print("1- f0 | Sumar")
		print("2- f1 | Restar")
		print("3- f2 | Multiplicar")
		print("4- f3 | Dividir")
		print("5- f4 | Longuitud de Circunferencia")
		print("6- f5 | Tablas de mumultiplicar")
		print("7- exit | Salir")
		print("8- clear | Limpiar")
		print("9- error | Leer errores")
		cal("------------------\n")
	elif button == 'f0':
		print()
		sumar()
		print()
	elif button == 'clear':
		import os
		os.system('clear')
	elif button == "f1":
		print()
		restar()
		print()
	elif button == "f2":
		print()
		multiplicar()
		print()
	elif button == "f3":
		print()
		dividir()
		print()
	elif button == "f4":
		print()
		longuitud()
		print()
	elif button == "f5":
		print()
		hm()
		print ()
	elif button == 'error':
		print()
		import os
		os.system("cat reb")
		print()
	
sys.exit()
