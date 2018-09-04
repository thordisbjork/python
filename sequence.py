#Bý til forlykkju sem rennur n oft í gegn. Reglan er að þrjár síðustu tölurnar eru lagðar saman.
#Fer inn í forlykkjuna og plúsar saman allar tölurnar. Síðan prentar það út summuna af tölunum þremur.
#Þarf fyrst að búa til sértilfelli innan forlykkjunnar fyrir fyrstu 3 ítranirnar.
#Eftir það verður tala1 að taka gildi tala2, tala2 að taka gildi tala3 og að lokum tekur tala3 nytt gildi sum sem er nýja talan í rununni
n = int(input("Enter the length of the sequence: ")) # Do not change this line

tala1 = 0
tala2 = 0
tala3 = 1
sum = 0

for i in range(n):
    if i < 3:
        sum = tala2 + tala3
        print(sum)
        tala1 = tala2
        tala2 = tala3
        tala3 = sum
    else:
        sum = tala1 + tala2 + tala3
        print(sum)
        tala1 = tala2
        tala2 = tala3
        tala3 = sum
    
