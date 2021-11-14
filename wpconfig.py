#!/usr/bin/env python3

import requests
import os
import threading
from colorama import Fore, Back, Style

linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE
batas = Style.RESET_ALL

def wpsetcon():
	
	Agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
	
	print(tai)
	
	print('''
	
 _    _       _____            ______     _            _   
| |  | |     /  __ \           |  _  \   | |          | |  
| |  | |_ __ | /  \/ ___  _ __ | | | |___| |_ ___  ___| |_ 
| |/\| | '_ \| |    / _ \| '_ \| | | / _ \ __/ _ \/ __| __|
\  /\  / |_) | \__/\ (_) | | | | |/ /  __/ ||  __/ (__| |_ 
 \/  \/| .__/ \____/\___/|_| |_|___/ \___|\__\___|\___|\__|
       | |                                                 
       |_|                                                 
                By : Wan5550
                Github : github.com/wannazid
                Blog : www.malastech.my.id
	''')
	print(batas)
	try:
		input_list = input('[#] List Site > ')
		input_save = input('[#] Result Name Detected (.txt) > ')
		print('\n')
		open_list = open(input_list,'r').read().splitlines()
		for site in open_list:
			try:
				satu = site+'/wp-admin/setup-config.php'
				req = requests.get(satu,headers=Agent)
				if '<title>WordPress &rsaquo; Setup Configuration File</title>' in req.text:
					print(f'{hijau}[!] {site} > Wp Setup Config Detected')
					savefile = open(input_save,'a').write(satu+'\n')
				else:
					print(f'{merah}[!] {site} > Wp Setup Config Not Detected')
					savefile = open('Wp Setup Config Not Detected.txt','a').write(satu+'\n')
			except requests.exceptions.HTTPError:
				print(f'{cyan}[!] {site} > Network Error')
	except requests.exceptions.HTTPError:
		print(f'{biru}[!] {site} > HTTP Error')
	print(batas)
	print(f'{tai}[✓] Successfully Save The File Detected Or Not Detected.')
	print(batas)
t = threading.Thread(target=wpsetcon)
t.start()
		