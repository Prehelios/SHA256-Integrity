#/usr/bin/python

"""Compare SUM"""

import os
import subprocess
import time

print ("\n")
print ("\t#####################################################################")
print ("\t#                                                                   #")                                 
print ("\t#                 Script de Comparaison de SHA256sum                #")     
print ("\t#                           Codé par ChessMaster                    #")                                                       
print ("\t#                             18 Avril 2017                         #")                                                                                                                                                            
print ("\t#                                                                   #")                                                                      
print ("\t#                                                                   #")
print ("\t#####################################################################")
print ("\n")
print (".....En Attente du SHA256sum :) Merci")

"""Commande PowerShell"""
os.chdir('C:\\Users\\admin\\Desktop')
o = subprocess.check_output("powershell.exe -noexit Get-Filehash kali-linux-2016.2-amd64.iso", shell=True)
print (o)

"""Entrer les Hashes"""
k = input("\n\nEntrez SHA256 ci-dessus : ").upper()
u = input("\n\nEntrez SHA256 officiel : ").upper()

"""Fonction compare"""

def compare_sum():
    if u == k :
        print ("\n\nLE LOGICIEL EST SAFE.")
    else :
        print ("\n\nLE LOGICIEL EST CORROMPU.")
        os.remove('C:\\Users\\admin\\Desktop\\kali-linux-2016.2-amd64.iso')
        print ("\n\nDELETE......")
        time.sleep(2.0)
        print (".........END")
        
        

"""VERDICT"""
compare_sum ()
