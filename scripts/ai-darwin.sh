#!/bin/sh
cd ../

# Define some constants for our AI server:
MAX_CHANNELS=999999
STATESERVER=4002
ASTRON_IP="127.0.0.1:7100"
EVENTLOGGER_IP="127.0.0.1:7198"
DISTRICT_NAME=Nuttyriver
BASE_CHANNEL=402000000

while [ true ]
do
    python3.9 -m toontown.ai.ServiceStart --base-channel $BASE_CHANNEL \
                     --max-channels $MAX_CHANNELS --stateserver $STATESERVER \
                     --astron-ip $ASTRON_IP --eventlogger-ip $EVENTLOGGER_IP \
                     --district-name $DISTRICT_NAME
done
