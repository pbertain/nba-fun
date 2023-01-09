#!/usr/bin/env python3
# File name: nba_time.py
# Description: Get the times of the NBA games for the night
# Author: Paul Bertain
# Date: 2023-01-08
# Source: python-script-template.py

import datetime as dt
import pytz

#fake_game_time           = '2023-01-08 17:00:00-08:00' # gameTimeLTZ

def game_time_format(game_time_from_api):
    game_time            = game_time_from_api
    pac                  = pytz.timezone('US/Pacific')
    utc                  = pytz.timezone('UTC')

    api_input            = '%Y-%m-%d %H:%M:%S%z'
    #api_output           = '%a %b %-d %-H:%M'
    api_output           = '%-H:%M'

    game_time_obj        = dt.datetime.strptime(game_time, api_input)
    #game_time_tz_utc     = utc.localize(game_time_obj, api_output)
    #game_time_tz_pac     = game_time_tz_utc.astimezone(pac)
    game_time_tz_pac     = game_time_obj.astimezone(pac)
    game_time_tz_pac_fmt = game_time_tz_pac.strftime(api_output)

    return(game_time_tz_pac_fmt)

#game_time_format(fake_game_time)