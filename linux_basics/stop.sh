#!/bin/bash
sudo docker ps -aq | xargs docker stop | xargs docker rm
