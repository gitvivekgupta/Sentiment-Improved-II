import csv
import json
from textblob import TextBlob
from google.cloud import translate
from spellchecker import SpellChecker

def get_neg_sub_score(neg_sub_score, theory):

    neg_sub_score += theory

    return neg_sub_score


def get_neu_sub_score(neu_sub_score, theory):

    neu_sub_score += theory

    return neu_sub_score


def get_pos_sub_score(pos_sub_score, theory):

    pos_sub_score += theory

    return pos_sub_score


def get_neg_score(neg_score, neg_sub_score, theory):
    
    neg_score += 10
    get_neg_sub_score(neg_sub_score, theory)

    return neg_score


def get_neu_score(neu_score, neu_sub_score, theory):
    
    neu_score += 20
    get_neu_sub_score(neu_sub_score, theory)

    return neu_score


def get_pos_score(pos_score, pos_sub_score, theory):
    
    pos_score += 30
    get_pos_sub_score(pos_sub_score, theory)

    return pos_score


def compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory):

    if(polarity >= .2):
        get_pos_score(pos_score, pos_sub_score, theory)
        
    elif(polarity > -.2 and polarity < .2):
        get_neu_score(neu_score, neu_sub_score, theory)
        
    else:
        get_neg_score(neg_score, neg_sub_score, theory)

