import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..","core"))

from inputandother_text import *
from scanizen_core import *


 
terminal_columns_size = os.get_terminal_size().columns
 
 
n = len(sys.argv)
print(n)
if n > 1:
	for i in range(1, n):
		if sys.argv[i] == "-nb":
			banner="SCANIZEN".center(terminal_columns_size)
				
else:
	banner = banner_maker(sc_name="Scanizen",description="Scan with nmap.",author="Onur Atakan ULUSOY",email="atadogan06@gmail.com")



main_menu_choices = menu_space() + \
 menu_maker(menu_number=1,menu_text="Local Scan")+ \
 menu_maker(menu_number=2,menu_text="Scan Target")+ \
 menu_space() + \
 menu_maker(menu_number=3,menu_text="Find IP From Domain Name")+ \
 menu_maker(menu_number=4,menu_text="Find IP From Domain Name BYPASS Cloudflare")+ \
 quit_menu_maker(mode="main")





local_submenu_choices = menu_space() + \
 menu_maker(menu_number=1,menu_text="IP Scan")+ \
 menu_maker(menu_number=2,menu_text="Basic Scan")+ \
 menu_maker(menu_number=3,menu_text="VULN Scan All Device")+ \
 menu_maker(menu_number=4,menu_text="Quick Scan All Device")+ \
 menu_maker(menu_number=5,menu_text="Full Scan All Device")+ \
 menu_seperator() + \
 menu_maker(menu_number=6,menu_text="Script DISCOVER Scan All Device")+ \
 menu_maker(menu_number=7,menu_text="Script DEFAULT-SAFE Scan All Device")+ \
 menu_maker(menu_number=8,menu_text="All FTP script Scan All Device")+ \
 menu_maker(menu_number=9,menu_text="All SSH script Scan All Device")+ \
 menu_maker(menu_number=10,menu_text="All HTTP script Scan All Device")+ \
 menu_seperator() + \
 menu_maker(menu_number=11,menu_text="Run routersploit auto scan")+ \
 menu_maker(menu_number=12,menu_text="Run routersploit console")+ \
 quit_menu_maker(mode="sub")





scantarget_submenu_choices = menu_space() + \
 menu_title(menu_title_text="NMAP") + \
  menu_maker(menu_number=1,menu_text="Quick Scan With Striker")+ \
  menu_maker(menu_number=2,menu_text="Basic Scan")+ \
  menu_maker(menu_number=3,menu_text="Version Scan")+ \
  menu_space() + \
  menu_maker(menu_number=4,menu_text="VULN Scan")+ \
  menu_maker(menu_number=5,menu_text="DISCOVERY Scan")+ \
  menu_maker(menu_number=6,menu_text="DNS-BRUTE Scan")+ \
  menu_maker(menu_number=7,menu_text="DOS Scan")+ \
  menu_maker(menu_number=8,menu_text="EXPLOIT Scan")+ \
  menu_maker(menu_number=9,menu_text="VERSION Scan")+ \
  menu_maker(menu_number=10,menu_text="DEFAULT-SAFE Scan")+ \
  menu_maker(menu_number=11,menu_text="Custom Script Category Scan")+ \
 menu_title(menu_title_text="ROUTERSPLOIT") + \
  menu_maker(menu_number=12,menu_text="Run routersploit auto scan")+ \
  menu_maker(menu_number=13,menu_text="Run routersploit console")+ \
 menu_title(menu_title_text="XSS Scan/Atack") + \
  menu_maker(menu_number=14,menu_text="XSS Scan")+ \
  menu_maker(menu_number=15,menu_text="XSS Payload Generator")+ \
 menu_title(menu_title_text="DICT Scan") + \
  menu_maker(menu_number=16,menu_text="Breacher")+ \
 menu_title(menu_title_text="SQL-Injection Scan") + \
  menu_maker(menu_number=17,menu_text="Sqlmap Wizard")+ \
  menu_maker(menu_number=18,menu_text="SQL-Injection vuln scan with ScanQLi")+ \
 menu_title(menu_title_text="Scan With Tool") + \
  menu_maker(menu_number=19,menu_text="Nikto Scan")+ \
  menu_maker(menu_number=20,menu_text="admin-panel-finder Scan")+ \
 menu_seperator() + \
  menu_maker(menu_number="auto",menu_text="AUTO MODE")+ \
 quit_menu_maker(mode="sub")





def start():
 os.system("clear")
 print(banner)
 print(main_menu_choices)
 main_menu()




def main_menu():
	choices_input = question_maker(mode="main")
	

	if choices_input == str("1"):
		clear()
		print("LOCAL SCAN".center(terminal_columns_size))
		local_submenu()
	elif choices_input == str("2"):
		clear()
		print("SCAN TARGET".center(terminal_columns_size))
		scantarget_submenu()
	elif choices_input == str("3"):
		clear()
		domain = input("Please enter domain-name to scan: ")
		starting_text_centered()
		
		os.system("host "+domain)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		start()
	elif choices_input == str("4"):
		clear()
		domain = question_maker(question_text="Please enter domain-name to scan: ")
		starting_text_centered()
		os.system("ruby HatCloud/hatcloud.rb -b "+domain)
		ended_text_centered()
		
		question_maker(mode="anykeytocontinue")
		start()
	elif choices_input == str("0"):
		exit()
	elif choices_input == str(""):
		print(main_menu_choices)
		main_menu()
	else:
		print("invalid option "+str(choices_input))
		main_menu()
		
	
def local_submenu():
	print(local_submenu_choices)
	choices_input = question_maker(mode="sub")
	
	if choices_input == str("1"):
		starting_text_centered()
		
		os.system("nmap -sn -n --open 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()
	if choices_input == str("2"):
		starting_text_centered()
		
		os.system("nmap -sCV 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()
		
	if choices_input == str("3"):
		starting_text_centered()
		
		os.system("nmap -sV --script vuln 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()		
		
	if choices_input == str("4"):
		starting_text_centered()
		
		os.system("nmap -T4 --max-retries 1 --max-scan-delay 20 --defeat-rst-ratelimit --open 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()
	if choices_input == str("5"):
		starting_text_centered()
		
		os.system("nmap -p- --max-retries 1 --max-rate 500 --max-scan-delay 20 -T4 -v 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()		 
	if choices_input == str("6"):
		starting_text_centered()
		
		os.system("nmap -v --script discovery 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
	if choices_input == str("7"):
		starting_text_centered()
		
		os.system("nmap -v --script default,safe 192.168.1.0/24")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
	if choices_input == str("8"):
		starting_text_centered()
		
		os.system(""""nmap -v --script "ftp-*" 192.168.1.0/24""")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
	if choices_input == str("9"):
		starting_text_centered()
		
		os.system("""nmap -v --script "ssh-*" 192.168.1.0/24""")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
	if choices_input == str("10"):
		starting_text_centered()
		
		os.system("""nmap -v --script "http-*" 192.168.1.0/24""")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
	if choices_input == str("11"):
		routerip = input("Please enter router ip to scan: ")
		starting_text_centered()
		
		os.system("python3 routersploit/rsf.py -m scanners/autopwn -s 'target "+routerip+"'")
		print(" ")
		run_routersploit = input("Run routersploit ? (yes/no)")
		if run_routersploit == str("yes"):
			print("RUNNING ROUTERSPLOIT\n".center(terminal_columns_size))
			start_routersploit()
			
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()
	if choices_input == str("12"):
		starting_text_centered()
		
		start_routersploit()
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		local_submenu()
	elif choices_input == str("0"):
		start()
	elif choices_input == str(""):
		print("invalid option "+str(choices_input))
		local_submenu()
	else:
		print("invalid option "+str(choices_input))
		local_submenu()



def scantarget_submenu():
	print(scantarget_submenu_choices)
	choices_input = question_maker(mode="sub")
	
	if choices_input == str("1"): #Striker
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		striker_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()	
	
	if choices_input == str("2"): #Basic
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		nmap_basic_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("3"): #Version
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		nmap_version_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("4"): #VULN
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		nmap_vuln_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()

	if choices_input == str("5"): #Discovery
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		os.system("nmap --script discovery "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("6"): #DNS-BRUTE
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		nmap_dns_brute_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("7"): #DOS
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		os.system("nmap --script dos "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("8"): #Exploit
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		os.system("nmap --script exploit "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("9"): #Script-Version
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		os.system("nmap -sV --script version "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("10"): #Default-Safe
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		os.system("nmap --script default,safe "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("11"): #Custom Category Script
		target = input("Please enter target (ip/domain-name) to scan: ")
		print(""" 
*** SCRIPT CATEGORY ***
auth
broadcast
brute
default
discovery
dos
exploit
external
fuzzer
intrusive
malware
safe
version
vuln
		""")
		script_category = input("Please enter category of script: ")
		starting_text_centered()
		
		os.system("nmap --script "+script_category+" "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("12"): #RouterSploit Auto scan and start
		routerip = input("Please enter router ip to scan: ")
		starting_text_centered()
		
		os.system("python3 routersploit/rsf.py -m scanners/autopwn -s 'target "+routerip+"'")
		print(" ")
		run_routersploit = input("Run routersploit ? (yes/no)")
		if run_routersploit == str("yes"):
			print("RUNNING ROUTERSPLOIT\n".center(terminal_columns_size))
			start_routersploit()
			
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("13"): #RouterSploit start
		starting_text_centered()
		
		start_routersploit()
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("14"): #XSS Scan
		target = input("Please enter url (e.g. http://testphp.vulnweb.com) to scan: ")
		starting_text_centered()
		
		xss_vuln_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("15"): #XSS Payload Generator
		starting_text_centered()
		
		os.system("cd XSS-LOADER && python payloader.py && cd ..")
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("16"): #Breacher
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		
		dict_scan_func(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("17"): #Sqlmap
		starting_text_centered()
		
		os.system("python3 sqlmap/sqlmap.py --wizard")
		
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("18"): #Sql intection scan
		target = input("Please enter url (e.g. http://testphp.vulnweb.com) to scan: ")
		starting_text_centered()
		
		sql_injection_vuln_scan(target=target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("19"): #Nikto
		target = input("Please enter target (ip/domain-name) to scan: ")
		starting_text_centered()
		
		os.system("perl nikto/program/nikto.pl -h "+target)
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("20"): #admin-panel-finder
		starting_text_centered()
		
		admin_panel_dict_scan_func()
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	if choices_input == str("auto"):
		starting_text_centered()
		
		auto_mode()
		
		ended_text_centered()
		question_maker(mode="anykeytocontinue")
		clear()
		scantarget_submenu()
	elif choices_input == str("0"):
		start()
	elif choices_input == str(""):
		print("invalid option "+str(choices_input))
		scantarget_submenu()
	else:
		print("invalid option "+str(choices_input))
		scantarget_submenu()











start()
