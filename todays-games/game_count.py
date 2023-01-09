#!/usr/bin/env python3
# File name: tonights_games.py
# Description: Get date and time for each 
# Author: Paul Bertain
# Date: 2023-01-08
# Source: python-script-template.py

# Query nba.live.endpoints.scoreboard and  list games in localTimeZone
from nba_api.live.nba.endpoints import scoreboard

def game_count():
    board = scoreboard.ScoreBoard()
    games = board.games.get_dict()
    game_count_for_tonite = len(games)
    return(game_count_for_tonite)

tonite_game_count = game_count()

if (tonite_game_count > 0):
    print("TRUE")
else:
    print("FALSE")
