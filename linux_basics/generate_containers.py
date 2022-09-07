#!/usr/bin/env python3
from string import Template
import sys
import random
import subprocess


def generate_password():

    adjective = ['young', 'old', 'big', 'small', 'light', 'heavy', 'sinister', 'evil', 'good', 'cuddly', 'poor', 'rich', 'handsome', 'ugly']
    noun = ['bird', 'dog', 'cat', 'horse', 'mouse', 'lion', 'hunter', 'soldier', 'lobster', 'shark', 'banana', 'orange']
    return adjective[random.randint(0, len(adjective) - 1)] + noun[random.randint(0, len(noun) - 1)] + str(random.randint(0, 1000))

def generate():

    rm = open("creds.txt", "w")
    rm.write("")
    rm.close()

    num_of_users = sys.argv[1]
    fd = open("Dockerfile.template", "r")
    data = fd.read()
    fd.close()

    form = Template(data)
    creds = open("creds.txt", "a")
    port = 2000
    for x in range(int(num_of_users)):
        new_fd = open("Dockerfile", "w")
        template = {}
        password = generate_password()
        template['password'] = password
        template['port'] = str(22)
        new_fd.write(form.substitute(template))
        creds.write(f"Container: {x}\n")
        creds.write(f"Password: {password}\n")
        new_fd.close()
        create_container = subprocess.Popen(["sudo", "docker", "build", "-t", f"challenge_{x}:Dockerfile", "."])
        create_container.wait()
        cmd = ["sudo", "docker", "run", "-d", "-p", f"{port}:22", f"challenge_{x}:Dockerfile"]
        start_container = subprocess.Popen(cmd)
        start_container.wait()
        port += 1
    creds.close()

if __name__ == "__main__":

    generate()
