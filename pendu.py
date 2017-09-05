#!/usr/bin/python
#-*- coding: utf-8 -*-
import fonctions

print ("""
██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗
██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║
██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║   ██║
██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
""")
print ("Fait par Maher ISNARD")

choice = input("1 - voir les scores // 2 - jouer \n")
if choice == 1:
    fonctions.get_scores()
else:
    name = raw_input("Quel est votre pseudo ? ")
    to_f = fonctions.solution_word
    fonctions.get_player(str(name))
    fonctions.generate_game(fonctions.pick_word())

    print ("Le mot est ", "".join(fonctions.wild_word))

    while fonctions.check_letter(raw_input("Choissisez une lettre ")):
        print ("Il vous reste {} vies".format(fonctions.life))
        print ("".join(fonctions.wild_word))

    if fonctions.life != 0:
        print ("Bravo vous avez gagner !")
        print ("Il vous reste ", fonctions.life, " vies et vous avez gagner ", fonctions.life, " points.")
        print ("Le mot etais donc ", "".join(fonctions.wild_word))
        fonctions.save_player(name, fonctions.life)
    else:
        print ("Malheuresement vous avez perdu !")
        print ("Le mot etais ", to_f)
        fonctions.save_player(name, 0)

    print ("fin de la partie !")