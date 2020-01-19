# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:26:33 2020

@author: bohmec
"""

import Dominion
import testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV = testUtility.NumVictory(player_names)
nC = testUtility.NumCurse(player_names)

#Define box
box = testUtility.GetBoxes(nV)

#Populate Supply Order
supply_order = testUtility.GetSupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.Pick(box)

#Sets up supply
#TEST SCENARIO: Swapping order of arguments nV and nC when setting up supply
testUtility.SupplySetup(supply, player_names, nC, nV)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.ConstructPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)