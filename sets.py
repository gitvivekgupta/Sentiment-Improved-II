import csv
import json



def get_neu_set_cc():

    neu_features = "./feature_files/neu_features.txt"
    neu_feature_file = open(neu_features, "r")

    neu_set_cc = set()

    for neu_word in neu_feature_file:

        neu_word = neu_word.lower()
        neu_set_cc.add(neu_word)

    return neu_set_cc


def get_neu_set_c():

    neu_features = "./feature_files/neu_features.txt"
    neu_feature_file = open(neu_features, "r")

    neu_set_c = set()

    for neu_word in neu_feature_file:

        neu_word = neu_word.lower()
        neu_set_c.add(neu_word)

    return neu_set_c


def get_neu_set():

    neu_features = "./feature_files/neu_features.txt"
    neu_feature_file = open(neu_features, "r")

    neu_set = set()

    for neu_word in neu_feature_file:

        neu_word = neu_word.lower()
        neu_set.add(neu_word)
        
    neg_set_cc = get_neg_set_cc()
    neu_set.difference_update(neg_set_cc)

    pos_set_cc = get_pos_set_cc()
    neu_set.difference_update(pos_set_cc)

    return neu_set


def get_neg_set_cc():

    neg_features = "./feature_files/neg_features.txt"
    neg_feature_file = open(neg_features, "r")

    neg_set_cc = set()

    for neg_word in neg_feature_file:

        neg_word = neg_word.lower()
        neg_set_cc.add(neg_word)

    return neg_set_cc


def get_neg_set_c():

    neg_features = "./feature_files/neg_features.txt"
    neg_feature_file = open(neg_features, "r")

    neg_set_c = set()

    for neg_word in neg_feature_file:

        neg_word = neg_word.lower()
        neg_set_c.add(neg_word)

    return neg_set_c


def get_neg_set():

    neg_features = "./feature_files/neg_features.txt"
    neg_feature_file = open(neg_features, "r")

    neg_set = set()

    for neg_word in neg_feature_file:

        neg_word = neg_word.lower()
        neg_set.add(neg_word)

    pos_set_c = get_pos_set_c()
    neg_set.difference_update(pos_set_c)

    neu_set_cc = get_neu_set_cc()
    neg_set.difference_update(neu_set_cc)

    return neg_set


def get_pos_set_cc():

    pos_features = "./feature_files/pos_features.txt"
    pos_feature_file = open(pos_features, "r")

    pos_set_cc = set()

    for pos_word in pos_feature_file:

        pos_word = pos_word.lower()
        pos_set_cc.add(pos_word)

    return pos_set_cc


def get_pos_set_c():

    pos_features = "./feature_files/pos_features.txt"
    pos_feature_file = open(pos_features, "r")

    pos_set_c = set()

    for pos_word in pos_feature_file:

        pos_word = pos_word.lower()
        pos_set_c.add(pos_word)

    return pos_set_c


def get_pos_set():

    pos_features = "./feature_files/pos_features.txt"
    pos_feature_file = open(pos_features, "r")

    pos_set = set()

    for pos_word in pos_feature_file:

        pos_word = pos_word.lower()
        pos_set.add(pos_word)

    neg_set_c = get_neg_set_c()
    pos_set.difference_update(neg_set_c)

    neu_set_c = get_neu_set_c()
    pos_set.difference_update(neu_set_c)

    return pos_set