
import os


import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))
from inputandother_text import *


#for check wordpress
import requests


def start_routersploit():
	os.system("python3 routersploit/rsf.py")



def striker_scan(target):
	printcentertext(text="STRIKER IS STARTED")
	os.system("python3 Striker/striker.py "+target)


def nmap_basic_scan(target):
	printcentertext(text="NMAP BASIC SCAN IS STARTED")
	os.system("nmap -A "+target)


def nmap_version_scan(target):
	printcentertext(text="NMAP VERSION SCAN IS STARTED")
	os.system("nmap -sV "+target)
	
	
def nmap_vuln_scan(target):
	printcentertext(text="NMAP VULN SCAN IS STARTED")
	os.system("nmap --script vuln "+target)
	
	
def nmap_dns_brute_scan(target):
	printcentertext(text="DNS BRUTE SCAN IS STARTED")
	os.system("nmap --script dns-brute -sn "+target)
	


def xss_vuln_scan(target):
	printcentertext(text="XSS VULN SCAN IS STARTED")
	os.system("python3 XSSCon/xsscon.py -u "+target)


def sql_injection_vuln_scan(target):
	printcentertext(text="SQL INTECTION VULN SCAN IS STARTED")
	os.system("python ScanQLi/scanqli.py -r -u "+target)

def dict_scan_func(target):
	printcentertext(text="DICT SCAN IS STARTED")
	os.system("cd Breacher && python breacher.py -u "+target+" && cd ..")

def admin_panel_dict_scan_func():
	os.system("cd admin-panel-finder && python2 admin_panel_finder.py && cd ..")

def wpseku_scan(wpseku_params):
	 printcentertext(text="WPSEKU IS STARTED")
	 os.system("python3 WPSeku/wpseku.py "+wpseku_params)


def is_wordpress(site_url, nocheck=None):
	if nocheck == True:
		return(True)
	else:
	 index = requests.get(site_url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"},verify=True if "https" in site_url else False)
	 if not "wp-" in index.text:
		 if question_maker(question_text="Site is not WordPress, pass wordpress scans ? (y)es or (n)o: ") != "y":
			 return(True)
		 else:
			 return(False)
	 else:
		 return(True)




def auto_mode():
	
	class site_scan:
		def __init__(self):
			self.domain = None
			self.https = None
			self.www = None
			self.site_url = None
			self.scan_mode = None
			self.site_is_wordpress = None
			self.xss_vuln_scan_mode = None
			self.sql_injection_vuln_scan_mode = None
			self.dict_scan_mode = None
			self.checking_plugin_code = None
			self.random_agent = None
			self.verbose_mode = None
			self.wpseku_params = ""
			self.auto_mode = None
			self.nmap_basic_scan_mode = None
			self.nmap_version_scan_mode = None
			self.nmap_dns_brute_scan_mode = None
			self.nmap_vuln_scan_mode = None
			self.striker_scan_mode = None
			self.get_info()
			
			
			
		def start_scan(self):
			if self.striker_scan_mode:
				striker_scan(target=self.domain)
			if self.site_is_wordpress:
				if self.checking_plugin_code:
					self.wpseku_params += "-s "
				if self.random_agent:
					self.wpseku_params += "-r "
				if self.verbose_mode:
					self.wpseku_params += "-v "
				self.wpseku_params += "-u "+self.site_url
				wpseku_scan(wpseku_params=self.wpseku_params)
			if self.nmap_basic_scan_mode:
				nmap_basic_scan(target=self.domain)
			if self.nmap_dns_brute_scan_mode:
				nmap_dns_brute_scan(target=self.domain)
			if self.nmap_version_scan_mode:
				nmap_version_scan(target=self.domain)
			if self.nmap_vuln_scan_mode:
				nmap_vuln_scan(target=self.domain)
			if self.dict_scan_mode:
				dict_scan_func(target=self.domain)
			if self.xss_vuln_scan_mode:
				xss_vuln_scan(target=self.site_url)
			if self.sql_injection_vuln_scan_mode:
				sql_injection_vuln_scan(target=self.site_url)
				
				
			
			
		def set_stealth_scan(self):
			self.dict_scan_mode = True
			self.verbose_mode = True
			self.random_agent = True
			self.striker_scan_mode = True
			self.nmap_basic_scan_mode = True
			self.nmap_version_scan_mode = True
			self.nmap_dns_brute_scan_mode = True
			
		def set_medium_scan(self):
			self.set_stealth_scan()
			self.xss_vuln_scan_mode = True
			self.nmap_vuln_scan_mode = True
		def set_aggressive_scan(self):
			self.set_medium_scan()
			self.sql_injection_vuln_scan_mode = True
			self.random_agent = None
			
		def scan_auto(self):
			self.site_is_wordpress=is_wordpress(site_url=self.site_url)
			if self.auto_mode == "1":
				self.set_stealth_scan()
			elif self.auto_mode == "2":
				self.set_stealth_scan()
			elif self.auto_mode == "3":
				self.set_aggressive_scan()
			self.start_scan()
		def get_info(self):
		 printcentertext(text="SITE INFO")
		 self.domain = question_maker(question_text="Please enter domain-name: ")
		 self.https = question_maker(question_text="""If http(s) please enter "y" else enter any key to continue: """)
		 self.www = question_maker(question_text="""If (www).domain.com please enter "y" else enter any key to continue: """)
		 self.site_url = ""
		 if self.https == "y":
			 self.site_url += "https://"
		 else:
			 self.site_url += "http://"
		 if self.www == "y":
		 	self.site_url += "www."
		 self.site_url += self.domain
		 printcentertext(text="SITE "+self.site_url)
		
		
		 printcentertext(text="SELECT SCAN MODE")
		 print(menu_maker(menu_number=1,menu_text="FULL AUTOMATIC")+menu_maker(menu_number=2,menu_text="SEMI AUTOMATIC"))
		 self.scan_mode = question_maker(question_text="Please enter your selection: ")
		
		
		 
		
		 if self.scan_mode == "1":
			 printcentertext(text="SELECT AUTOMATIC MODE")
			 print(menu_maker(menu_number=1,menu_text="STEALTH")+menu_maker(menu_number=2,menu_text="MEDIUM")+menu_maker(menu_number=3,menu_text="AGGRESSIVE"))
			 self.auto_mode = question_maker(question_text="Please enter your selection: ")
			 self.scan_auto()
		 elif self.scan_mode == "2":
			 printcentertext(text="SCAN SETTINGS")
			 
			 self.striker_scan_mode = True if question_maker(question_text="""If you want striker scan please enter "y" else enter any key to continue: \n""") == "y" else None
			 self.nmap_basic_scan_mode = True if question_maker(question_text="""If you want nmap basic scan please enter "y" else enter any key to continue: \n""") == "y" else None
			 self.nmap_version_scan_mode = True if question_maker(question_text="""If you want nmap version scan please enter "y" else enter any key to continue: \n""") == "y" else None
			 self.nmap_dns_brute_scan_mode = True if question_maker(question_text="""If you want nmap dns brute scan please enter "y" else enter any key to continue: \n""") == "y" else None
			 self.nmap_vuln_scan_mode = True if question_maker(question_text="""If you want nmap vuln scan please enter "y" else enter any key to continue: \n""") == "y" else None
			 
			 
			 self.xss_vuln_scan_mode = True if question_maker(question_text="""If you want checking xss vuln please enter "y" else enter any key to continue: \n""") == "y" else None
			 self.sql_injection_vuln_scan_mode = True if question_maker(question_text="""If you want checking sql injection vuln please enter "y" else enter any key to continue: \n""") == "y" else None
			 self.dict_scan_mode =True if question_maker(question_text="""If you want checking dict please enter 1 else enter any key to continue: \n""") == "y" else None
			 
			 
			 
			 
			 
			 self.site_is_wordpress=is_wordpress(site_url=self.site_url)
			 if self.site_is_wordpress:
				 self.checking_plugin_code = True if question_maker(question_text="""If you want checking wordpress plugin code for wordpress scan please enter "y" else enter any key to continue: """) == "y" else None
				 self.random_agent = True if question_maker(question_text="""If you want checking scan with random agent for wordpress scan please enter "y" else enter any key to continue: """) == "y" else None
				 self.verbose_mode = True if question_maker(question_text="""If you want open verbose mode for wordpress scan please enter "y" else enter any key to continue: """) == "y" else None
				 self.wpseku_params = ""
				 if self.checking_plugin_code == "1":
					 self.wpseku_params += "-s "
				 if self.random_agent == "1":
					 self.wpseku_params += "-r "
				 if self.verbose_mode == "1":
					 self.wpseku_params += "-v "
				 self.wpseku_params += "-u "+self.site_url
				
			 self.start_scan()
				
	the_site = site_scan()
	
