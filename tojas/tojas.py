import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..","core"))

from inputandother_text import *
from tojas_core import *

 
 
terminal_columns_size = os.get_terminal_size().columns
 
 
n = len(sys.argv)
if n > 1:
	for i in range(1, n):
		if sys.argv[i] == "-nb":
			banner="TOJAS".center(terminal_columns_size)
		if sys.argv[i] == "-gui":
			os.system("cd .. && python3 lib/tojas_gui.py")
			exit()
				
else:
	banner = banner_maker(sc_name="Tojas",description="Create trojan with metasploit.",author="Onur Atakan ULUSOY",email="atadogan06@gmail.com")




main_menu_choices = menu_space() + \
menu_maker(menu_number=1,menu_text="Windows")+ \
menu_maker(menu_number=2,menu_text="Start Msfconsole")+ \
menu_maker(menu_number=3,menu_text="ifconfig")+ \
quit_menu_maker(mode="main")



windows_submenu_choices = """
1) Start (EXE)  
 
0) Quit sub menu
"""




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
		print("WINDOWS".center(terminal_columns_size))
		windows_submenu()
	elif choices_input == str("2"):
		
		start_msfconsole()

		input("Press any key to continue...")
		start()
	elif choices_input == str("3"):
		start_ifconfig()
		input("Press any key to continue...")
		start()
	elif choices_input == str("0"):
		exit()
	elif choices_input == str(""):
		print(main_menu_choices)
		main_menu()
	else:
		print("invalid option "+str(choices_input))
		main_menu()
		
	
def windows_submenu():
	print(windows_submenu_choices)
	choices_input = input("Please enter sub option: ")
	
	if choices_input == str("1"):
		start_windows_exploit()
		input("Press any key to continue...")
		clear()
		windows_submenu()		

	elif choices_input == str("0"):
		start()
	elif choices_input == str(""):
		windows_submenu()
	else:
		print("invalid option "+str(choices_input))
		windows_submenu()



start()
