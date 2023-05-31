#!/bin/bash

FILE="kalipage.id"

if test -f "$FILE"; then
        # start old instance
        OLD_ID=`cat $FILE`
	echo "Stopping docker #$OLD_ID"
        docker stop $OLD_ID
        docker rm $OLD_ID
fi

# start new instance
DOCKER_ID=`docker run -d --restart always -p 8001:80 kali-page:latest`
echo "Started docker $DOCKER_ID"
echo $DOCKER_ID > $FILE
