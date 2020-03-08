#delta.py delta=b*2-4ac
a,b,c=input("digite os coeficientes:").split()
a=float(a)
b=float(b)				
c=float(c)
delta=b**2-4*-a*c
duasr=delta>0
umar=delta==0
semr=delta<0
if(delta>0):
	print("possui duas raizes e"+str(duasr))

if(delta==0):
	print("possui duas raizes e"+str(umar))

if(delta<0):
	print("possui duas raizes e"+str(semr))









						
