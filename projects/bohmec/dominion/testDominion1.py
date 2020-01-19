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
#TEST SCENARIO: changed nV to nC, effecting the amount of "Garden" cards initialized in testUtilty.GetBoxes
box = testUtility.GetBoxes(nC)

#Populate Supply Order
supply_order = testUtility.GetSupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.Pick(box)

#Sets up supply
testUtility.SupplySetup(supply, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.ConstructPlayers(player_names)

#Play the game
testUtility.Play(supply, supply_order, players, trash)

#Final score
testUtility.Score(players)