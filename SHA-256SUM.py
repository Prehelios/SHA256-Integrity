#/usr/bin/python

"""Compare SUM"""

import os
import subprocess


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
print (".....En Attente du SHA256zum :) Merci")

"""Commande PowerShell"""
os.chdir('C:\\Users\\admin\\Desktop')
o = subprocess.check_output("powershell.exe -noexit Get-Filehash kali-linux-2016.2-amd64.iso", shell=True)
print (o)

"""Entrer des Hashes"""
k = input("Entrez SHA256 ci-dessus : ")
u = input("Entrez SHA256 site officiel : ")


"""Fonction compare"""

def compare_sum():
    if u == k :
        print ("LE LOGICIEL EST SAFE.")
    else :
        print ("LE LOGICIEL EST CORROMPU.")
        os.remove('C:\\Users\\admin\\Desktop\\kali-linux-2016.2-amd64.iso')
        print ("DELETE")
        

"""VERDICT"""
compare_sum ()
