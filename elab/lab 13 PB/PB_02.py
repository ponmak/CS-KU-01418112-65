# 02 Blackjack (Easy) 

DECK = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def busted_checker(ls: list):
    scores = 0
    for i in ls:
        if scores <= 16:
            for j in range(len(DECK)):
                if DECK[j] == i and not i in ['J','Q','K']:
                    scores += j + 1
                elif DECK[j] == i and i in ['J','Q','K']:
                    scores += 10
        
    if scores > 21:
        scores = "busted"

    return scores

player = int(input())

player_hand = []
for i in range(player):
    player_hand.append(input().split(" "))

for i in range(player):
    print(busted_checker(player_hand[i]))