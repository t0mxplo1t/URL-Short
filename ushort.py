import pyshorteners,os

from pyshorteners import Shortener

os.system("pip install pyshorteners")
os.system("clear")

def banner():
	print("""
 █    ██  ██▀███   ██▓      ██████  ██░ ██  ▒█████   ██▀███  ▄▄▄█████▓
 ██  ▓██▒▓██ ▒ ██▒▓██▒    ▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒
▓██  ▒██░▓██ ░▄█ ▒▒██░    ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░
▓▓█  ░██░▒██▀▀█▄  ▒██░      ▒   ██▒░▓█ ░██ ▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░
▒▒█████▓ ░██▓ ▒██▒░██████▒▒██████▒▒░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░    ░
 ░░░ ░ ░   ░░   ░   ░ ░   ░  ░  ░   ░  ░░ ░░ ░ ░ ▒    ░░   ░   ░
   ░        ░         ░  ░      ░   ░  ░  ░    ░ ░     ░
\033[30;46mThe Simple URL Shortener is written using Python\033[0m\n""")
banner()

x = Shortener()
url = input("\033[1;36mEnter long URL \033[0m: ")
y = x.tinyurl
z = y.short(url)
print("\033[1;36mConversion results \033[0m:",z)
