#!/usr/bin/env python3
# File name: game_slate.py
# Description: Get date and time for each 
# Author: Paul Bertain
# Date: 2023-01-08
# Source: python-script-template.py

# Query nba.live.endpoints.scoreboard and  list games in localTimeZone
from datetime import datetime, timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard

import nba_time

# sample date: 'gameTimeUTC': '2023-01-08T03:00:00Z',

f = "{time_of_game}: {awayTeam} @ {homeTeam}" # @ {gameTimeLTZ}" 

board = scoreboard.ScoreBoard()
games = board.games.get_dict()
game_count = len(games)

for game in games:
    gameTimeLTZ       = str(parser.parse(game["gameTimeUTC"]))
    game_time = nba_time.game_time_format(gameTimeLTZ)
    print(f.format(time_of_game=game_time, awayTeam=game['awayTeam']['teamName'], homeTeam=game['homeTeam']['teamName']))
