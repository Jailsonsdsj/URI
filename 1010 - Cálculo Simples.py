a=str(input()).split(); b=str(input()).split()
c1=int(a[0]); q1=int(a[1]); v1=float(a[2])
c2=int(b[0]); q2=int(b[1]); v2=float(b[2])
tt=(q1*v1)+ (q2*v2)
print("VALOR A PAGAR: R$ {:.2f}".format(tt))
