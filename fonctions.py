import donnees
import pickle
import os
from random import randint

wild_word = []
solution_word = []
life = donnees.lifes

def pick_word():
    max = donnees.word_list.__len__()
    min = 0
    index = randint(min, max - 1) #on genere un nombre aleatoire avec la taille de la liste
    to_find = donnees.word_list[index]
    return to_find

def generate_game(to_find):
    for letter in to_find:
        wild_word.append('*')
        solution_word.append(letter)

def check_letter(letter):
    global life
    i = 0;
    while letter in solution_word:
        valid = solution_word.index(letter)
        solution_word[valid] = "*"
        wild_word[valid] = letter
        i += 1
    if i == 0:
        life -= 1
    if "*" in wild_word:
        return True
    else:
        return False

def get_player(name):
    if os.path.exists('scores'):
        with open('scores', 'rb') as scores:
            mes_scores = pickle.Unpickler(scores)
            scores = mes_scores.load()
            if name in scores:
                player_s = scores[name]
                player_n = name
            else:
                scores[name] = 0
                player_n = 0
                player_s = 0
    else:
        score = {}
        score[name] = 0
        player_n = name
        player_s = 0
        with open('scores', 'wb') as scores:
            mes_scores = pickle.Pickler(scores)
            mes_scores.dump(score)
    return player_n, player_s

def save_player(name, points):
    if os.path.exists('scores'):
        global score_s
        global total
        with open('scores', 'rb') as score:
            mes_scores = pickle.Unpickler(score)
            score_s = mes_scores.load()
            if name in score_s:
                total = points + score_s[name]
            else:
                total = points
        score_s[name] = total
        with open('scores', 'wb') as score:
            mes_scores = pickle.Pickler(score)
            mes_scores.dump(score_s)

def get_scores():
    if os.path.exists('scores'):
        with open('scores', 'rb') as score:
            mes_scores = pickle.Unpickler(score)
            scores = mes_scores.load()
            print scores
    else:
        print "Aucun scores pour le moment !"