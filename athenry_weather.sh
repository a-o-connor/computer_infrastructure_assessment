#! /bin/bash
wget https://prodapi.metweb.ie/observations/athenry/today -O ./data/weather/`date +"%Y%m%d_%H%M%S"`_athenry.json 
