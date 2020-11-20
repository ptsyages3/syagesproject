#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Scripte python pertant de générer 200 étudiant absent en SQL
# Pour les testes dans la base de donnée
# Abdou Kandji- IUT Villetaneuse 20/21, VERT-SYAGES



import random
from  random import randint, sample
import  json
import time

tableau_etu=[]
tableau_etu200=[]
tab_matieres=["maths","francais","anglais","physique","informatique","langue"]


def extraire_etudiant():
    with open("id_user_e.txt","r") as f_etus:
        i=1
        p=f_etus.readline().rstrip('),\n').strip('(')
        while (p!=""):
            tableau_etu.append(p)
            i+=1
            p=f_etus.readline().rstrip('),\n').strip('(')
        f_etus.close()

def date():
    #print(int(time.time())) '2020-11-25 19:53:17'
    return "'"+time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(random.randint(1555000000, int(time.time()))))+"'"

def affiche_insert_abs_rtd():
    '''
    Affiche le script sql sur la console
    
    '''
    text="INSERT INTO `absenceretard`(`idUser`, `Date`, `Justif`, `Data`, `Historique`, `Drapeau`) VALUES "
    print(text)
    i=1
    while i < 201:
        if(randint(0,5)<3): j="'absence justifiée'"
        else : j="'absence non justifiée'"
        l="("+tableau_etu200[i-1]+", "+date()+", "+str(randint(0,1))+", "+j+", 'vide', 0),"
        print(l)
        i+=1

extraire_etudiant()
tableau_etu200=sample(tableau_etu, 200)
#affiche_insert_abs_rtd()


def genere_fichier_absretard_sql():
    '''
    Ecrit le script sql dans le fichier absretart.sql
    
    '''
    text="-- IUT Viletaneuse, Groupe Vert 2020-2021 : SYAGES PROJECT\n"
    text+="--            Abdou KANDJI\n"
    text+="-- Base de données : `bdd_syages`\n"
    text+="-- Structure de la table `absenceretard`\n\n"
    text+='SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";\n'
    text+="START TRANSACTION;\n"
    text+='SET time_zone = "+00:00";\n\n'
    
    text+="DROP TABLE IF EXISTS `absenceretard`;\n"
    text+="CREATE TABLE IF NOT EXISTS `absenceretard` (\n"
    text+="  `idAbs` int(11) NOT NULL AUTO_INCREMENT,\n"
    text+="  `idUser` int(11) NOT NULL,\n"
    text+="  `Datetheure` datetime NOT NULL,\n"
    text+="  `Justif` int(11) NOT NULL,\n"
    text+="  `Data` text NOT NULL,\n"
    text+="  `Historique` text NOT NULL,\n"
    text+="  `Drapeau` tinyint(4) NOT NULL,\n"
    text+="   PRIMARY KEY (`idAbs`)\n"
    text+=") ENGINE=MyISAM AUTO_INCREMENT=240 DEFAULT CHARSET=utf8;\n"

    text+="--\n"
    text+="-- Déchargement des données de la table `absenceretard`\n"
    text+="--\n"
    
    text+="INSERT INTO `absenceretard`(`idUser`, `Datetheure`, `Justif`, `Data`, `Historique`, `Drapeau`) VALUES\n"
    
    
    f = open("absretart.sql", "w")
    f.write(text)
    f.write("(11111116, '2020-03-14 05:57:02', 1, 'absence non justifiée', 'vide', 0)")
    i=2
    while i < 201:
        if(randint(0,5)<3): j="'absence justifiée'"
        else : j="'absence non justifiée'"
        l=",\n("+tableau_etu200[i-1]+", "+date()+", "+str(randint(0,1))+", "+j+", 'vide', 0)"
        f.write(l)
        i+=1
    f.write(";")
    f.close()

genere_fichier_absretard_sql()


# In[ ]:




