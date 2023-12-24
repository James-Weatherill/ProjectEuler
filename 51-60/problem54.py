player1 = []
player2 = []
wins = 0

file = open("assets/0054_poker.txt","r")
cards = str(file.readlines()).replace("['","").replace("']","").split(" ")
                                                                                              
ind = -10
while len(player1)!=1000:
    ind += 10
    player1.append([cards[ind], cards[ind+1], cards[ind+2], cards[ind+3], cards[ind+4]])
    player2.append([cards[ind+5], cards[ind+6], cards[ind+7], cards[ind+8], cards[ind+9]])
    
for i in range(1000):
    
    player1Cards = [int(player1[i][0][:-1]),int(player1[i][1][:-1]),int(player1[i][2][:-1]),int(player1[i][3][:-1]),int(player1[i][4][:-1])]
    player2Cards = [int(player2[i][0][:-1]),int(player2[i][1][:-1]),int(player2[i][2][:-1]),int(player2[i][3][:-1]),int(player2[i][4][:-1])]
    
    player1Cards.sort()
    player2Cards.sort()
    
    player1Suits = set(player1[i][0][-1])
    player1Suits.add(player1[i][1][-1])
    player1Suits.add(player1[i][2][-1])
    player1Suits.add(player1[i][3][-1])
    player1Suits.add(player1[i][4][-1])
    
    player2Suits = set(player2[i][0][-1])
    player2Suits.add(player2[i][1][-1])
    player2Suits.add(player2[i][2][-1])
    player2Suits.add(player2[i][3][-1])
    player2Suits.add(player2[i][4][-1]) 
    
    if len(set(player1Cards))==2 or len(set(player2Cards))==2:
        if len(set(player1Cards))<len(set(player2Cards)):
            wins += 1
            
    elif len(player1Suits)==1 or len(player2Suits)==1:
        if len(player1Suits)<len(player2Suits):
            wins += 1
            
    elif (player1Cards[0]==player1Cards[1]-1 and player1Cards[0]==player1Cards[2]-2 and player1Cards[0]==player1Cards[3]-3 and player1Cards[0]==player1Cards[4]-4) or (player2Cards[0]==player2Cards[1]-1 and player2Cards[0]==player2Cards[2]-2 and player2Cards[0]==player2Cards[3]-3 and player2Cards[0]==player2Cards[4]-4) or (player1Cards[0]==2 and player1Cards[1]==3 and player1Cards[2]==4 and player1Cards[0]==14) or (player2Cards[0]==2 and player2Cards[1]==3 and player2Cards[2]==4 and player2Cards[0]==14):
        if (player1Cards[0]==player1Cards[1]-1 and player1Cards[0]==player1Cards[2]-2 and player1Cards[0]==player1Cards[3]-3 and player1Cards[0]==player1Cards[4]-4) or (player1Cards[0]==2 and player1Cards[1]==3 and player1Cards[2]==4 and player1Cards[0]==14):
            wins += 1
            
    elif len(set(player1Cards))==3 or len(set(player2Cards))==3:
        toak1 = False
        toak2 = False
        for val in range(3):
            if player1Cards[val]==player1Cards[val+2]:
                toak1 = True
            if player2Cards[val]==player2Cards[val+2]:
                toak2 = True
        if toak1 and not toak2:
            wins += 1
        
#         elif not toak1 and not toak2:
#             if len(set(player1Cards))==3 and len(set(player2Cards))!=3:
#                 wins += 1
                
    elif len(set(player1Cards))==4 or len(set(player2Cards))==4:
        for val in range(4):
            if player1Cards[val]==player1Cards[val+1]:
                player1Pair = player1Cards[val]
            if player2Cards[val]==player2Cards[val+1]:
                player2Pair = player2Cards[val]
        if player1Pair>player2Pair:
            wins += 1
        elif player1Pair==player2Pair:
            for val in range(-1,-5,-1):
                if player1Cards[val]!=player2Cards[val] and player1Cards[val]!=player1Pair and player2Cards[val]!=player2Pair:
                    if player1Cards[val]>player2Cards[val]:
                        wins += 1
                    break
                    
    else:
        for val in range(-1,-5,-1):
            if player1Cards[val]!=player2Cards[val]:
                if player1Cards[val]>player2Cards[val]:
                    wins += 1
                break    
                
print(wins)

