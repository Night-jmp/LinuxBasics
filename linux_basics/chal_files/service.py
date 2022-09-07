#!/usr/bin/env python3

import os
import threading

def check_level5():
    PATH = "/home/level5/"
    while True:
        if os.path.isdir(PATH + "ctf_is_life"):
            fd = open(PATH + "flag.txt", "w")
            fd.write("fitsec{mkd!r_!s_c00l_!_gu3ss}\n")
            fd.close()
            break

def check_level6():
    PATH = "/home/level6/"
    while True:
        try:
            fd = open(PATH + "message_for_admin", "r")
            data = fd.read()
            if data == "pls give flag ty\n":
                flag = open(PATH + "flag.txt", "w")
                flag.write("fitsec{0k_h3r3_u_g0}\n")
                flag.close()
                break
            fd.close()
        except:
            continue

def check_level7():
    PATH = "/home/level7/"
    while True:
        if os.path.exists(PATH + "perm_check"):
            if int(oct(os.stat(PATH + "perm_check").st_mode)[5:]) == 740:
                fd = open(PATH + "flag.txt", "w")
                fd.write("fitsec{p3rm!ss!0ns_0n_fl33k}\n")
                fd.close()     
                break

def check_level8():
    PATH = "/home/level8/"
    while True:
        if os.path.isdir(PATH + "removeme"):
            continue
        else:
            fd = open(PATH + "flag.txt", "w")
            fd.write("fitsec{d3l3t!ng_d!r3ct0r!3s}\n")
            fd.close()
            break

def check_level9():
    PATH = "/home/level9/"
    while True: 
        if os.path.isdir(PATH + "removeme"):
            continue
        else:
            fd = open(PATH + "flag.txt", "w")
            fd.write("fitsec{r3m0v!ng_l0ts_0f_f!l3s}\n")
            fd.close()
            break

if __name__ == "__main__":
    lvl5 = threading.Thread(target=check_level5)
    lvl6 = threading.Thread(target=check_level6)
    lvl7 = threading.Thread(target=check_level7)
    lvl8 = threading.Thread(target=check_level8)
    lvl9 = threading.Thread(target=check_level9)
    lvl5.start()
    lvl6.start()
    lvl7.start()
    lvl8.start()
    lvl9.start()
