# Morse Translator by TrollSkull © 2020

import time, os, sys

loop = 1
ter = ""

def ini():
	print(chr(27)+"[1;36m"+"""
  	    MORSE     TRANSLATOR
  	     
          .--.                   .---.
      .---|__|           .-.     |~~~|
   .--|===|--|_          |_|     |~~~|--.
   |  |===|  |'\     .---!~|  .--|   |--|
   |%%|   |  |.'\    |===| |--|%%|   |  |
   |%%|   |  |\.'\   |   | |__|  |   |  |
   |  |   |  | \  \  |===| |==|  |   |  |
   |  |   |__|  \.'\ |   |_|__|  |~~~|__|
   |  |===|--|   \.'\|===|~|--|%%|~~~|--|
   ^--^---'--^    `-'`---^-^--^--^---'--' 
""")
	print(chr(27)+"[1;37m"+"""____________________________________________""")
	
	print(chr(27)+"[1;37m"+"\n           Created by "+chr(27)+"[1;32m"+"@TrollSkull\n")

	print(chr(27)+"[1;30m"+"[INFO] Type \"show options\" to show command\n")
	
ini()

while (loop == 1):
	ter = str(input(chr(27)+"[1;0;37m"+"Morse "+chr(27)+"[1;36m"+">>"+chr(27)+"[1;37m"+" "))
	if ter == "translator":
		print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;32m"+"✓"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Translator activated")
		def morse(txt):
			encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'|'}
               
			decrypt = {v: k for k, v in encrypt.items()}
    
			if '-' in txt:
				print("") # Morse a Idioma
				return ''.join(decrypt[i] for i in txt.split())
				print("")
			else:
				print("") # Idioma a Morse
				return ' '.join(encrypt[i] for i in txt.upper())
				print("")
		
		code = input(chr(27)+"[1;0;37m"+"\nMorse/Translator "+chr(27)+"[1;36m"+">>"+chr(27)+"[1;37m"+" ")
		print(morse(code))
		o = morse(code)
	elif ter == "clear":
		if sys.platform == "win32":
			os.system("cls")
			ini()
		else:
			os.system("clear")
			ini()
	elif ter == "about":
		print(chr(27)+"[1;36m"+"""
   Author:"""+chr(27)+"[1;37m"+""" 	     	 TrollSkull
   """+chr(27)+"[1;36m"+"""Version:"""+chr(27)+"[1;37m"+"""   	 	 Alpha 1.1"""+chr(27)+"[1;36m"+"""
   Name:"""+chr(27)+"[1;37m"+"""		 Morse Translator"""+chr(27)+"[1;36m"+"""
   Contact:"""+chr(27)+"[1;37m"+"""		 trollskull.contact@gmail.com
   
   """+chr(27)+"[1;32m"+"""if you find any errors or problems, please contact author
		""")
	elif ter == "show options":
		print(chr(27)+"[1;36m"+"""
      COMMAND                        DESCRIPTION"""+chr(27)+"[1;37m"+"""
  ---------------	-------------------------------------
   translator		 Translate to Morse and vice versa
  
   change log		 The list of changes in this version
   about		 Show information about this program
   clear		 Clean the terminal
   exit			 Exit the program\n""")
	elif ter == "exit":
		print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;31m"+"!"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Exiting program\n")
		exit()
	elif ter == "change log":
		print(chr(27)+"[1;36m"+"\nChanges 1.1:\n")
		print(chr(27)+"[1;37m"+"""Added \"clear\" command
		
Change in program structure
""")
	else:
		print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;31m"+"!"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Command \"" + ter + "\" not found\n")
