"""
programme table de multiplication

"""

nombre = int(input("entre le nombre de la table de multiplication "))


for i in range(1,nombre+1):
    #print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print(end=' ')
    for j in range(1,10):
           print("\t",j, "x", i, "=", i*j, "\n")

      

#print("\t\t\t")


