import os


for x in range(100):
    os.mkdir("flag_in_here")
    working_dir = os.getcwd()
    os.chdir(working_dir + "/flag_in_here")

fd = open("flag.txt", "w")
fd.write("fitsec{pls_d0nt_cd}\n")
fd.close()
