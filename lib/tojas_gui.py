import tkinter

import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..","core"))

from inputandother_text import *
from tojas_core import *
 
mainwindow = tkinter.Tk()
 
 
banner = True
 
 
 
n = len(sys.argv)
if n > 1:
	for i in range(1, n):
		if sys.argv[i] == "-nb":
			banner = False
		if sys.argv[i] == "-zm":
			mainwindow.attributes("-fullscreen", True)
		elif sys.argv[i] == "-ic":
			mainwindow.state("iconic")
		elif sys.argv[i] == "-ops":
			mainwindow.wm_attributes("-alpha", 0.3)






mainwindow.title("TOJAS")


mainwindow.geometry("500x250")
mainwindow.resizable(True,True)


if not banner == False:
	banner = tkinter.Label(text="Script Name: Tojas\n Description: Create trojan with metasploit.\nAuthor: Onur Atakan ULUSOY\nEmail: atadogan06@gmail.com")
else:
	banner = tkinter.Label(text="TOJAS")

banner.pack()



def clear_main_menu_options():
	windows_button.pack_forget()
	startmsfconsole_button.pack_forget()
	ifconfig_button.pack_forget()
	quit_button.pack_forget()


def clear_windows_sub_menu_options():
	tojas_startexe_button.pack_forget()
	windows_quit_button.pack_forget()
	start()



def start_windows_submenu():
	 clear_main_menu_options()
	 tojas_startexe_button.pack(side=tkinter.LEFT,pady=10,padx=20,ipady=10,ipadx=5)
	 windows_quit_button.pack(side=tkinter.RIGHT,pady=10,padx=20,ipady=10,ipadx=5)
	 
	
def start_exe():
	mainwindow.withdraw()
	os.system("clear")
	start_windows_exploit()
	mainwindow.deiconify()
	
def start_msfconsole_menu():
	mainwindow.withdraw()
	os.system("clear")
	start_msfconsole()
	mainwindow.deiconify()
	 
def start_ifconfig_submenu():
	start_ifconfig()


windows_button =  tkinter.Button(text="Windows",command=start_windows_submenu)
startmsfconsole_button =  tkinter.Button(text="Start Msfconsole",command = start_msfconsole_menu)
ifconfig_button =  tkinter.Button(text="İfconfig",command=start_ifconfig_submenu)
quit_button =  tkinter.Button(text="QUIT",command = exit)


tojas_startexe_button =  tkinter.Button(text="Start (EXE)",command=start_exe)
windows_quit_button =  tkinter.Button(text="Quit sub menu",command = clear_windows_sub_menu_options) 


def start():

	windows_button.pack(side=tkinter.LEFT,pady=10,padx=20,ipady=10,ipadx=5)

	startmsfconsole_button.pack(side=tkinter.LEFT,pady=10,padx=20,ipady=10,ipadx=5)

	ifconfig_button.pack(side=tkinter.LEFT,pady=10,padx=20,ipady=10,ipadx=5)

	quit_button.pack(side=tkinter.RIGHT,pady=10,padx=20,ipady=10,ipadx=5)









start()


os.system("clear")
mainwindow.mainloop()
