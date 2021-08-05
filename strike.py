#usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system ("apt install figlet")
os.system("clear")
os.system ("figlet Strike")

print("""
(browsing about the site)
(site hakkında bilgi toplama)
        (1) Site Bilgi Toplama)
        (2) Site Port Taraması)
        (3) Normal Tarama)
        (q) Çıkış)
""")

islemno = raw_input ("işlem numarasına giriniz: ")
if islemno=="1":
        hedefsite=raw_input("""hedef site giriniz: """)
        os.system ("whois "+hedefsite)
elif islemno=="2":
        hedefsite=raw_input ("""hedef site giriniz: """)
        os.system ("nmap "+hedefsite)
elif islemno=="3":
        hedefsite=raw_input ("""hedef site giriniz: """)
        os.system("nmap -v -A "+hedefsite)
if islemno=="q":
        os.system("figlet iyi Gunler")

tem = raw_input("""
Ekran Temizlensin mi? [Y/n]: """)

if(tem == "y"):
        os.system("clear")

elif(tem == "n"):
        print("""
Güle Güle""")
