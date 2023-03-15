#!/usr/bin/python3

hashes="" #file with hashes in them

import importlib.util

packageC = "colorama"
packageH = "hashlib"
is_presentC = importlib.util.find_spec(packageC)
is_presentH = importlib.util.find_spec(packageH)
if is_presentC is None:
	print(packageC +" is not installed, installing now")
	os.system("pip3 install colorama --break-system-packages")
if is_presentH is None:
	print(packageH +" is not installed, installing now")
	os.system("pip3 install hashlib --break-system-packages")

import hashlib
import colorama
from colorama import init, Fore #used for the colors listed below

init()

GREEN = Fore.GREEN
RED   = Fore.RED
BLUE  = Fore.BLUE
CYAN  = Fore.CYAN
RESET = Fore.RESET

a = 0
passfile=input(f"{BLUE}Password file full path (ex: /usr/share/wordlists/rockyou.txt):\n{RESET}")
hashes=input(f"{BLUE}MD5 Hash to crack? ex: 85c73111b30f9ede8504bb4a4b682f48\n{RESET}")
for password in open(passfile, encoding="utf-8", errors="ignore"):
	try:
		if hashlib.md5((password.strip()+"\n").encode()).hexdigest() == hashes:
			print(f"\n{GREEN} Found Hash:{RED}", password)
	except:
		a+=1
