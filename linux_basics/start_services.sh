#!/bin/bash

python3 /root/service.py &

/usr/sbin/sshd -D
