#!/bin/bash

NBA_PATH="/Users/paulb/Dropbox/home/tech/nba/nba-fun/todays-games"
NBA_DATE=`date '+%a %b %d'`
NBA_TIME=`date '+%l:%M%p'`
NBA_PYTHON="/usr/bin/python3"
NBA_SCRIPT="${NBA_PATH}/game_slate.py"
GAME_COUNT="${NBA_PATH}/game_count.py"
NBA_GAME_SLATE=`${NBA_PYTHON} ${NBA_SCRIPT}`
GAME_COUNT_CHECK=`${NBA_PYTHON} ${GAME_COUNT}`
MSG_HEADER=`echo -e "${NBA_DATE} ${NBA_TIME}:\r\r"`

if [ "${GAME_COUNT_CHECK}" > 0 ]
then
    /Users/paulb/bin/imessage.sh -t GROUP -r "NBA Stats" -m "${MSG_HEADER}${NBA_GAME_SLATE}"
else
    echo "No games today"
fi
