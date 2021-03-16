#!/bin/bash

clear




###################################################################
#Script Name    : Mixon                                                   
#Description    : THE HACKMIX.
#Author         :Onur Atakan ULUSOY                                            
#Email          :atadogan06@gmail.com
###################################################################

printf '###################################################################
#Script Name    : Mixon                                                   
#Description    : THE HACKMIX.
#Author         :Onur Atakan ULUSOY                                            
#Email          :atadogan06@gmail.com
###################################################################
'

install-mixon-on-termux () {
	pkg install python2 python nmap
	git submodule update --init --recursive
	printf '
	*** NOW PLEASE WRITE DOWN FOR THE USING: ./mixon.py or python3 mixon.py
	'
	exit
}

install-mixon-on-other-linux () {
	apt install python2 python3 pip nmap
	git submodule update --init --recursive
	printf '
	*** NOW PLEASE WRITE DOWN FOR THE USING: ./mixon.py or python3 mixon.py
	'
	exit
}


only-sub-github-repo () {
	git submodule update --init --recursive
	printf '
	*** NOW PLEASE WRITE DOWN FOR THE USING: ./mixon.py or python3 mixon.py
	'
	exit
	}



main-menu () {
# main menu
PS3='Please enter install option: '
options=("TERMUX" "OTHER LINUX" "ONLY INSTALL SUB GITHUB REPO" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "TERMUX")
            clear
            install-mixon-on-termux
            ;;
        "OTHER LINUX")
            clear
            install-mixon-on-other-linux
            ;;
        "ONLY INSTALL SUB GITHUB REPO")
            clear
            only-sub-github-repo
            ;;
        "Quit")
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
}

main-menu
