import os
import sys
import time

os.system ('clear')
time.sleep(2)
os.system ('figlet Zaiin')
time.sleep(2)
merah='\33[31;1m'
print ('*********************************')
print (merah+'[Author = Zain]')
print (merah+'[wa =00000000')
print ('*********************************')
print ('[1] Install Bahan')
print ('[2] Exit')
time.sleep(2)
pilih = input (' Pilihan :')
if pilih == '1':
	print ('Proses Mengistall')
	os.system ('pkg update - y && pkg upgrade -y')
	time.sleep(2)
	os.system ('pkg install nano -y')
	time.sleep(2)
	os.system ('pkg install figlet -y')
	time.sleep(2)
	os.system ('pkg install python2 -y')
	print ('Proses Selesai')
	time.sleep(5)
elif pilih == '2':
	print ('Terimakasih')
	os.system ('exit')
	

