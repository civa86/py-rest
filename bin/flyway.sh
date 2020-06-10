#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "Usage: ./flyway.sh <ENV> <OPERATION>"
    exit 1
fi

if [ -z "$2" ]
  then
    echo "Usage: ./flyway.sh <ENV> <OPERATION>"
    exit 1
fi

if [ ! -f resources/database/config/$1.conf ]; then
    echo "Configuration file for env '$1' not found!"
    exit 1
fi

docker run -v $(pwd)/resources/database:/flyway/resources flyway/flyway:6.0.1 -X -configFiles=resources/config/$1.conf $2
