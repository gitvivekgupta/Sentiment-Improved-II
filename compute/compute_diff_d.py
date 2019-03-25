import csv
import json
from textblob import TextBlob
from google.cloud import translate
from spellchecker import SpellChecker


def neg_score(polarity, neg_score):
    
    neg_score += 10

    return neg_score


def neu_score(polarity, neu_score):
    
    neu_score += 20

    return neu_score


def pos_score(polarity, pos_score):
    
    pos_score += 30

    return pos_score


def compute_score(polarity, pos_score, neu_score, neg_score):

    if(polarity >= .2):
        pos_score(pos_score)
        
    elif(polarity > -.2 and polarity < .2):
        neu_score(neu_score)
        
    else:
        neg_score(neg_score)

