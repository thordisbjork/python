#Þarf að búa til while lykkju sem tekur inn input þangað til að inputtið er neikvæð tala. 
#Inní while lykkjunni athuga ég síðan hvort inputið sé stærra en talan biggest. 
#Talan biggest er breyta sem byrjar í núll og tekur alltaf nýtt gildi ef talan sem notandinn setur inn
#er stærri en gilidið sem breytan er þegar búin að taka. 
#Þegar notandinn setur inn neikvæða tölu þá hættir hann í while lykkjunni og 
#skrifar út gildið á breytunni biggest.

num = int(input("Input an int: "))

biggest = 0
while num >= 0:
    if num > biggest:
        biggest = num   
    num = int(input("Input an int: "))

print("Biggest: ",biggest)
