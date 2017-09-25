#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
print("An Online-Judge Date Crawler OJDC for Local Judge OALJ developed by kZime && Margatroid with ❤❤")
fst = input("你想安装OJDC吗? (y/n， 默认为y)")
if fst != 'n':
    os.system('sudo cp cogs.py /usr/bin/oalj')
    os.system('sudo cp loj.py /usr/bin/loj')
    os.system('sudo cp syzoj.py /usr/bin/syzoj')
    ask = input("是否安装pip, axel以及库文件?(y/n, 默认为y)")
    if ask != 'n':
        os.system("sudo apt-get install python3-pip")
        os.system("sudo apt-get install axel")
        os.system("sudo pip3 install urllib3[socks]")
        os.system("sudo pip3 install colorama")
        os.system("sudo pip3 install requests")
        os.system("sudo pip3 install psutil")
else:
    sec = input("你想卸载OJDC吗? (y/n, 默认为n)")
    if sec != 'n':
        os.system('sudo rm cogs.py /usr/bin/oalj')
        os.system('sudo rm loj.py /usr/bin/loj')
        os.system('sudo rm syzoj.py /usr/bin/syzoj')
