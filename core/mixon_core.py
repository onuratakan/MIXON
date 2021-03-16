
import sys
import os



def start_tojas():
	os.system("cd tojas  && python3 tojas.py -nb && cd ..")

def start_tojas_gui():
	os.system("python3 lib/tojas_gui.py -nb")



def start_scanizen():
	os.system("cd scanizen  && python3 scanizen.py -nb && cd ..")

def start_doser():
	os.system("cd doser  && python3 doser.py -nb && cd ..")


def start_routersploit():
	os.system("python3 routersploit/rsf.py")
