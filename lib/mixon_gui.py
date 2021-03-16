import tkinter

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..","lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..","core"))

from inputandother_text import *
from mixon_core import *
 
 
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






mainwindow.title("MIXON")


mainwindow.geometry("500x250")
mainwindow.resizable(True,True)


if not banner == False:
	banner = tkinter.Label(text="Script Name: Mixon\n Description: THE HACKMIX.\nAuthor: Onur Atakan ULUSOY\nEmail: atadogan06@gmail.com")
else:
	banner = tkinter.Label(text="MIXON")

banner.pack()


def start_tojas_menu():
	mainwindow.withdraw()
	os.system("clear")
	start_tojas_gui()
	os.system("clear")
	mainwindow.deiconify()



tojas_button =  tkinter.Button(text="TOJAS",command = start_tojas_menu)
tojas_button.pack(side=tkinter.LEFT,pady=10,padx=20,ipady=10,ipadx=5)


scanizen_button =  tkinter.Button(text="SCANIZEN")
scanizen_button.pack(side=tkinter.LEFT,pady=10,padx=20,ipady=10,ipadx=5)

quit_button =  tkinter.Button(text="QUIT",command = mainwindow.destroy)
quit_button.pack(side=tkinter.RIGHT,pady=10,padx=20,ipady=10,ipadx=5)







os.system("clear")
mainwindow.mainloop()
