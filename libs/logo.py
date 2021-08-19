# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
   
███╗░░██╗██████╗░██╗░░░░░██╗░░░░░░░██╗██╗░░░░░░░██████╗██████╗░░█████╗░███╗░░░███╗
████╗░██║╚════██╗██║░░░░░██║░░░░░░██╔╝██║░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░████║
██╔██╗██║░█████╔╝██║░░░░░██║░░░░░██╔╝░██║█████╗╚█████╗░██████╔╝███████║██╔████╔██║
██║╚████║░╚═══██╗██║░░░░░██║░░░░░███████║╚════╝░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██║░╚███║██████╔╝███████╗███████╗╚════██║░░░░░░██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═╝░░╚══╝╚═════╝░╚══════╝╚══════╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝"""



def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "Code by N3ll4"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> a big thank you goes to my Community")
