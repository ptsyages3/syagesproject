#!/usr/bin/env python
# coding: utf-8

# In[2]:
#-- IUT Viletaneuse, Groupe Vert 2020-2021 : SYAGES PROJECT
#--            Abdou KANDJI
#-- Base de données : `bdd_syages`

import random
from  random import randint, sample
import  json
import time

tableau_prenoms=[]
tableau_noms=[]

tab_matieres=["maths","francais","anglais","physique","informatique","svt"]

def extraire_personnes():
    # lecture noms et prenoms
    with open("prenoms.txt","r") as f_prenoms:
        i=1
        p=f_prenoms.readline().rstrip('\n')
        while (p!=""):
            tableau_prenoms.append(p)
            i+=1
            p=f_prenoms.readline().rstrip('\n')
        f_prenoms.close()

    with open("noms.txt","r") as f_noms:
        i=1
        p=f_noms.readline().rstrip('\n')
        while (p!=""):
            tableau_noms.append(p)
            i+=1
            p=f_noms.readline().rstrip('\n')
        f_noms.close()
        
def matiere():
    tab=sample(tab_matieres, 3)
    return "'"+tab[0]+", "+tab[1]+", "+tab[2]+"', '', '', "
def num6ou7():
    return randint(6, 7)*100000000+randint(0, 10000)*10000
def role():
    if(randint(0, 100)<80) : return 'e'
    return 'p'
def oui_non():
    if(randint(0, 100)<50) : return "'non', "
    return "'oui', "
def genererPwd():
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"
    passwd = ""
    for i in range(12):
        passwd = passwd + element[random.randint(0, len(element) - 1)]
    return passwd

#idUser=11111111+1
#login= prenom+idUser
#genererPwd()
#Nom=f_noms
#NomEpouse=null
#Prénom=f_prenoms
#Photo=p1+1
#Téléphone = 07 00 00 00 00 ou 06 00 00 00 00 + i
#Mail=premon.nom@gmail.com
#idEtablissement=1
#Role= e ou p
#InscriptionMatiere=tab_matieres
#InscriptionPeda=""
#InfoPrivee=""
#InfoRedoublement = oui ou non (prof non)
#Perqonnalisation = ""
#Data = vide
#Historique = vide
#Drapeau=0

def affiche_insert_users():
    text="INSERT INTO `users`(`idUser`, `Login`, `MotDePasse`, `Nom`, `NomEpouse`, `Prénom`, `Photo`, `Téléphone`, `Mail`, `idEtablissement`, `Role`, `promo`,`InscriptionMatiere`, `InscriptionPeda`, `InfoPrivee`, `InfoRedoublement`, `Perqonnalisation`, `Data`, `Historique`, `Drapeau`)VALUES \n"
    print(text)
    idUser=11111111
    i=0
    while i < 300:
        r=role()
        promo=0
        if(r=='p'):
            o_n="'non', "
        else :
            o_n=oui_non()
            promo= randint(120211, 120212)
        idu=idUser+i
        l="("+str(idu)+", '"+str(tableau_prenoms[(i-1)%500])+str(idu)+"', '"+str(genererPwd())+"', '"+tableau_noms[(i-1)%500]+"', '', '"+tableau_prenoms[(i-1)%500]+"', 'p"+str(i)+"', 0"+str(num6ou7()+i)+", '"
        l+=tableau_prenoms[(i-1)%500]+"."+tableau_noms[(i-1)%500]+"@edu.universite.fr', 1, '"+r+"', "+str(promo)+","+matiere()+o_n+" 'rien', 'vide', 'vide', 0),"
        print(l)
        i+=1

        
        
        
        
def gener_insert_users():
    f = open("users.sql", "w")
    text="INSERT INTO `users`(`idUser`, `Login`, `MotDePasse`, `Nom`, `NomEpouse`, `Prénom`, `Photo`, `Téléphone`, `Mail`, `idEtablissement`, `Role`, `promo`,`InscriptionMatiere`, `InscriptionPeda`, `InfoPrivee`, `InfoRedoublement`, `Perqonnalisation`, `Data`, `Historique`, `Drapeau`)VALUES \n"
    f.write(text)
    idUser=11111111
    i=0
    while i < 600:
        r=role()
        promo=0
        if(r=='p'):
            o_n="'non', "
        else :
            o_n=oui_non()
            promo= randint(120211, 120212)
        idu=idUser+i
        l="("+str(idu)+", '"+str(tableau_prenoms[(i-1)%500])+str(idu)+"', '"+str(genererPwd())+"', '"+tableau_noms[(i-1)%500]+"', '', '"+tableau_prenoms[(i-1)%500]+"', 'p"+str(i)+"', 0"+str(num6ou7()+i)+", '"
        l+=tableau_prenoms[(i-1)%500]+"."+tableau_noms[(i-1)%500]+"@edu.universite.fr', 1, '"+r+"', "+str(promo)+","+matiere()+o_n+" 'rien', '', '', 0),\n"
        f.write(l)
        i+=1
    f.close()
extraire_personnes()

affiche_insert_users()
gener_insert_users()


# In[ ]:




