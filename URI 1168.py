seq=[]
n=int(input())
cont=cont_tot=0

for i in range(n):
    aux=str(input())
    seq.append(aux)

for i in range(len(seq)):
    cont = seq[i].count("0") + seq[i].count("6") + seq[i].count("9")
    cont_tot += cont * 6

    cont = seq[i].count("1")
    cont_tot += cont * 2

    cont = seq[i].count("2") + seq[i].count("3") + seq[i].count("5")
    cont_tot += cont * 5

    cont = seq[i].count("4")
    cont_tot += cont * 4

    cont = seq[i].count("7")
    cont_tot += cont * 3

    cont = seq[i].count("8")
    cont_tot += cont * 7

    print("{} leds".format(cont_tot))
    cont_tot = 0