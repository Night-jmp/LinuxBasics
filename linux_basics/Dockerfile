FROM ubuntu:latest
RUN apt update && apt install  openssh-server sudo -y
RUN apt install -y vim
RUN apt install -y binutils


RUN useradd --create-home --shell /bin/bash level0
RUN  echo 'level0:uglysoldier151' | chpasswd
COPY ./level0_chal/ /home/level0
RUN chmod u-w /home/level0
RUN chmod 1444 /home/level0/flag.txt


RUN useradd --create-home --shell /bin/bash level1
RUN  echo 'level1:uglysoldier151' | chpasswd
COPY ./level1_chal/ /home/level1
RUN chmod u-w /home/level1
RUN chmod 1444 /home/level1/.flag.txt


RUN useradd --create-home --shell /bin/bash level2
RUN  echo 'level2:uglysoldier151' | chpasswd
COPY ./level2_chal/ /home/level2
RUN chmod u-w /home/level2
RUN chmod 1444 /home/level2/*


RUN useradd --create-home --shell /bin/bash level3
RUN  echo 'level3:uglysoldier151' | chpasswd
COPY ./level3_chal/ /home/level3
RUN chmod u-w /home/level3
RUN chmod u+x /home/level3/runme


RUN useradd --create-home --shell /bin/bash level4
RUN  echo 'level4:uglysoldier151' | chpasswd
COPY ./level4_chal/ /home/level4
RUN chmod u-w /home/level4
RUN chown level4:level4 /home/level4/runme
RUN chmod -x /home/level4/runme


RUN useradd --create-home --shell /bin/bash level5
RUN  echo 'level5:uglysoldier151' | chpasswd
COPY ./level5_chal/ /home/level5


RUN useradd --create-home --shell /bin/bash level6
RUN  echo 'level6:uglysoldier151' | chpasswd
COPY ./level6_chal/ /home/level6


RUN useradd --create-home --shell /bin/bash level7
RUN  echo 'level7:uglysoldier151' | chpasswd
COPY ./level7_chal/ /home/level7


RUN useradd --create-home --shell /bin/bash level8
RUN  echo 'level8:uglysoldier151' | chpasswd
COPY ./level8_chal/ /home/level8


RUN useradd --create-home --shell /bin/bash level9
RUN  echo 'level9:uglysoldier151' | chpasswd
COPY ./level9_chal/ /home/level9
RUN chown -R level9:level9 /home/level9/removeme


RUN useradd --create-home --shell /bin/bash level10
RUN  echo 'level10:uglysoldier151' | chpasswd
COPY ./level10_chal/ /home/level10


RUN useradd --create-home --shell /bin/bash level11
RUN  echo 'level11:uglysoldier151' | chpasswd
COPY ./level11_chal/ /home/level11


RUN useradd --create-home --shell /bin/bash level12
RUN  echo 'level12:uglysoldier151' | chpasswd
COPY ./level12_chal/ /home/level12


RUN useradd --create-home --shell /bin/bash level13
RUN  echo 'level13:uglysoldier151' | chpasswd
COPY ./level13_chal/ /home/level13


RUN useradd --create-home --shell /bin/bash level14
RUN  echo 'level14:uglysoldier151' | chpasswd
COPY ./level14_chal/ /home/level14

COPY ./chal_files/service.py /root
COPY ./start_services.sh /root

RUN service ssh start

EXPOSE 22

CMD ["/root/start_services.sh"]

