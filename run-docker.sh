#!/bin/bash

docker run -d --restart on-failure -p 8001:80 kali-page:latest
