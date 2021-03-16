#!/bin/bash

clear


# need a nmap,dnsutils(host)




###################################################################
#Script Name	: ScanizeN                                                                                             
#Description	: Scan with nmap.                                                                                                                                                                           
#Author       	:Onur Atakan ULUSOY                                                
#Email         	:atadogan06@gmail.com                                           
###################################################################

printheader () {
printf '###################################################################\n#Script Name	: ScanizeN\n#Description	: Scan with nmap.\n#Author       	:Onur Atakan ULUSOY\n#Email         	:atadogan06@gmail.com\n###################################################################\n\n\n'
}


return-func () {
echo ""
read -n 1 -s -r -p "Press any key to continue"
clear
$1
}



# local
local-submenu () {
  local title="LOCAL"
  printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title"
  echo ""

  local PS3='Please enter sub option: '
  local options=("IP Scan" "A Scan All Device" "Sub menu quit")
  local opt
  select opt in "${options[@]}"
  do  
      case $opt in
        "IP Scan")
            echo "STARTING THE IP SCAN"
            nmap -sn -n -v --open 192.168.1.0/24
            return-func "local-submenu"
            ;;
        "A Scan All Device")
            echo "STARTING THE A SCAN ALL DEVICE"
            nmap -A -v 192.168.1.0/24
            return-func "local-submenu"
            ;;
          "Sub menu quit")
              clear
              main-menu
              ;;
          *) echo "invalid option $REPLY";;
      esac
     
  done
}


# scan from ip
scan-from-target-submenu () {
  local title="SCAN FROM TARGET"
  printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title"
  echo ""

  local PS3='Please enter sub option: '
  local options=("A SCAN" "Sub menu quit")
  local opt
  select opt in "${options[@]}"
  do  
      case $opt in
        "A SCAN")
            echo "STARTING THE A SCAN"
            local ip
            read -p 'Please enter target (ip/domain-name) to scan: ' ip
            nmap -A -v $ip
            return-func "scan-from-target-submenu"
            ;;
          "Sub menu quit")
              clear
              main-menu
              ;;
          *) echo "invalid option $REPLY";;
      esac
     
  done
}

main-menu () {
# main menu
printheader
PS3='Please enter main option: '
options=("LOCAL SCAN" "SCAN FROM TARGET" "FIND IP FROM DOMAIN NAME" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "LOCAL SCAN")
            clear
            local-submenu
            ;;
        "SCAN FROM TARGET")
            clear
            scan-from-target-submenu 
            ;;
        "FIND IP FROM DOMAIN NAME")
            local domain
            read -p 'Please enter domain-name to scan: ' domain
            host $domain
            return-func "main-menu"
            ;;
        "Quit")
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
}

main-menu
