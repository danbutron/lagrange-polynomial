# importamos la libreria Sympy para algebra computacional
import sympy as sp

#declaramos las variables y arreglos necesarios
x = sp.Symbol('x')
i = 0
a = [0]
b = [0]
l = [x]
den=[1]
pl = x

#solicitamos el numero de datos
tam = int(input('numero de datos = '))

#insercion de datos
for i in range(0,tam):
	if i == 0:
		a[0]= int(input('x 0 = '))
		b[0]= int(input('y 0 = '))
	else:
		texx = 'x ' + str(i) + '= '
		texy = 'y ' + str(i) + '= '
		a.append(int(input(texx)))
		b.append(int(input(texy)))
#impresion de x & y
print(a)
print(b)
ecu = x
#calculo de L's
for i in range(0,tam):
	if i == 0:
		for j in range(1,tam):
			print(l[0])
			if i == 1:
				l[0] = x - a[j]
				den[0] = a[0] - a[j]
			else:
				l[0] = (l[0])*(x - a[j])
				den[0] = den[0]*(a[0] - a[j])
		l[0]= l[0] / x
		
	else:
		l.append(x)
		den.append(1)
		for j in range(0,tam):
			if i == 0:
				l[i] =x - a[0]
				den[i] = a[i] - a[j]
			else:
				if j != i:
					l[i] = (l[i])*(x - a[j])
					den[i] = den[i]*(a[i] - a[j])
		l[i]= l[i] / x
	l[i] = l[i]/den[i]
	print('Calculo de L',i)
	print(sp.expand(l[i]))
	print(' ')

#Calculo de PL
print('PL :')
for i in range(0,tam):
	if i == 0:
		pl = b[0] * l[0]
	else:
		pl = pl + (b[i]*l[i])
print(sp.simplify(pl))

	
		

