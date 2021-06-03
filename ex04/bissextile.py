def annee():
    annee = int(input("saisir une année \n"))
    if (annee%4==0 and  annee%100!=0 or annee%400==0):
        print("l'anneée est est bissextile")
    else:
        print("l'année n'est pas bissextible")
annee()
        
