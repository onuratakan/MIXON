import os



terminal_columns_size = os.get_terminal_size().columns

def starting_text_centered():
	print(" ")
	print("\033[0;30;47m STARTING \033[0m\n".center(terminal_columns_size))


def ended_text_centered():
	print(" ")
	print("\033[0;30;47m ENDED \033[0m \n".center(terminal_columns_size))

def printcentertext(text):
	print(" ")
	print("\033[1;37;40m"+text.center(terminal_columns_size)+"\033[0;37;40m")
	print(" ")

def banner_maker(sc_name,description,author,email):
	return("""\033[1;37;40mScript Name    : """+"\033[5;37;40m"+sc_name+"\033[0;37;40m \033[1;37;40m"+"""\n"""+"""Description    : """+description+"""\n"""+"""Author         : """+author+"""\n"""+"""Email          : """+email+"""\033[0;37;40m""")

def question_maker(question_text=None,mode=None):
	
	if question_text == None:
		if mode == "main":
			question_text = "Please enter main option: "
		elif mode == "sub":
			question_text = "Please enter sub option: "
		elif mode == "anykeytocontinue":
			question_text = "Press any key to continue..."
	
	return(input("""\033[1;33;40m[?] """+question_text+"""\033[0m"""))


def menu_maker(menu_number,menu_text):
	return("\033[1;37;40m"+str(menu_number)+") "+menu_text+"\033[0;37;40m\n")
	

def quit_menu_maker(mode):
	if mode == "main":
		quit_menu_maker_result = "\n\033[1;31;40m0) Quit\033[0m \n"
	elif mode == "sub":
		quit_menu_maker_result = "\n\033[1;31;40m0) Quit sub menu\033[0m \n"
	return(quit_menu_maker_result)


def menu_space():
	return("\n")

def menu_seperator():
	return("\n"+"*** \n"+"\n")

def menu_title(menu_title_text):
	return("\n\033[1;34;40m"+"*** "+menu_title_text+" ***"+" \n"+"\033[0m\n")


def decode(string):
	return string.encode('utf-8')




def clear():
	os.system("clear")
