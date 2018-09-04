#Bý til forlykkju sem rennur n oft í gegn. Reglan er að þrjár síðustu tölurnar eru lagðar saman.
#Fer inn í forlykkjuna og plúsar saman allar tölurnar. Síðan prentar það út summuna af tölunum þremur.
#Eftir það verður tala1 að taka gildi tala2, tala2 að taka gildi tala3 og að lokum tekur tala3 nytt gildi sum sem er nýja talan í rununni

n = int(input("Enter the length of the sequence: ")) # Do not change this line

tala1 = 1
tala2 = 0
tala3 = 0
sum = 0

for in range(n):
    sum = tala1 + tala2 + tala3
    print("sum: ",sum)
    print("gamla tala1:",tala1)
    print("gamla tala2:",tala2)
    print("gamla tala3:",tala3)
    tala1 = tala2
    tala2 = tala3
    tala3 = sum
    print("Nýja tala1:",tala1)
    print("nýja tala2:",tala2)
    print("nýja tala3:",tala3)

