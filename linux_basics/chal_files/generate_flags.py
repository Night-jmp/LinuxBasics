fake_flags = ["fitsec{im_the_real_flag}\n", "fitsec{no_im_the_real_flag}\n", "fitsec{realest_flag_evarrrr}\n"]

real_flag = "fitsec{s0rt_!t_0ut}\n"

i = 0
for x in range(1000):
    
    fd = open(f"flag{x}.txt", "w")
    fd.write(fake_flags[i%3])
    i += 1
    fd.close()

fd = open("flag497.txt", "w")
fd.write(real_flag)
fd.close()
