from cards import *
ntrials = 1000
winlist = []
for i in range(ntrials):
    adeck = deck()
    bdeck = deck()
    adeck.shuffle()
    bdeck.shuffle()
    awins = 0
    bwins = 0
    while adeck.cardsleft()or bdeck.cardsleft() > 0:
        acard=adeck.dealcard()
        bcard=bdeck.dealcard()
        if acard.value()==bcard.value():
            continue
        if acard.value()> bcard.value() :
            awins= awins + 2
        else:
              bwins = bwins + 2
    difference = abs(awins - bwins)
    winlist.append(difference)

for x in range(0,52):
    if x % 2 != 0:
        continue
    print(x, winlist.count(x)/ntrials)
    
