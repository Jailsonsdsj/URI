values=(input())
values=values.split(" ");a=float(values[0]);b=float(values[1]);c=float(values[2])
triangulo=(a*c)/2
circulo=3.14159*(c**2)
trapezio=((a+b)*c)/2
quadrado=b*b
retangulo=a*b
print("TRIANGULO: %.3f"%triangulo)
print("CIRCULO: %.3f"%circulo)
print("TRAPEZIO: %.3f"%trapezio)
print("QUADRADO: %.3f"%quadrado)
print("RETANGULO: %.3f"%retangulo)


