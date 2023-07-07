nbrmin = int(input("Entrez un min:"))
nbrmax = int(input("Entrez un max:"))

for n in range(nbrmin,nbrmax + 1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
                print(n)