#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),"lib"))
from inputandother_text import *


 
 
sys.path.append(os.path.join(os.path.dirname(__file__), "core"))

from mixon_core import *


terminal_columns_size = os.get_terminal_size().columns				

banner = banner_maker(sc_name="Mixon",description="THE HACKMIX",author="Onur Atakan ULUSOY",email="atadogan06@gmail.com")


main_menu_choices = menu_space() + \
menu_maker(menu_number=1,menu_text="Tojas (Build a exploit with metasploit)")+ \
menu_maker(menu_number=2,menu_text="Scanizen (Network scan tool)")+ \
menu_maker(menu_number=3,menu_text="Doser (Usefull ddos tool)")+ \
quit_menu_maker(mode="main")





n = len(sys.argv)

if n > 1:
	for i in range(1, n):
		if sys.argv[i] == "-nb":
			banner="MIXON".center(terminal_columns_size)
		if sys.argv[i] == "-gui":
			os.system("python3 lib/mixon_gui.py")
			exit()






def start():
 os.system("clear")
 print(banner)
 print(main_menu_choices)
 main_menu()

def clear():
	os.system("clear")



def main_menu():
	choices_input = question_maker(mode="main")
	

	if choices_input == str("1"):
		clear()
		
		start_tojas()
		

		start()
	elif choices_input == str("2"):
		clear()
		
		start_scanizen()
		
		start()
	elif choices_input == str("3"):
		clear()
		
		start_doser()
		

		start()
	elif choices_input == str("0"):
		exit()
	elif choices_input == str(""):
		print(main_menu_choices)
		main_menu()
	else:
		print("invalid option "+str(choices_input))
		main_menu()
		









start()

