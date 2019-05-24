#24/05/2019 TP
#FT @ generator
import random
def theProgram():
    player = input(str("What is the name of your player?"))
    suffixNum = random.randint(0,9)
    suffixArray = ["Role","esque","ology","SZN","Mindset","Effect","Ctrl","Ability","Essence","Section"] 
    prefixNum = random.randint(0,7)
    prefixArray = ["Prime","Classy","Ftbl","Magical","Lowkey","WorldClass","Super","Prolific"]
    presuf = random.randint(0,1)
    if presuf == 0:
        playerAt = (player+suffixArray[suffixNum])
    else:
        playerAt = (prefixArray[prefixNum]+player)
    print (playerAt)
    theProgram()
theProgram()
