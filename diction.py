import csv
import json


def google_english_2_hindi(token, e2h_dict):

    mm = 0
    
    for vv in e2h_dict:
        
        if(vv < len(e2h_dict)):
            
            eng_tok = e2h_dict[vv][0]
            hin_tok = e2h_dict[vv][1]
            vv += 1

            if(token == eng_tok):

                english_2_hindi_tok = hin_tok
                return english_2_hindi_tok
            else:
                return 0


def google_hindi_2_english(token, h2e_dict):

    ll = 0
    
    for ss in h2e_dict:
        
        if(ll < len(h2e_dict)):
            
            hin_tok = h2e_dict[ll][0]
            eng_tok = h2e_dict[ll][1]
            ll += 1

            if(token == hin_tok):

                hindi_2_english_tok = eng_tok
                return hindi_2_english_tok
            else:
                return 0


def hindi_2_english(token, h2e_list):

    kk = 0
    
    for ss in h2e_list:
        
        if(kk < len(h2e_list)):
            
            eng_tok = h2e_list[kk][0]
            hin_tok = h2e_list[kk][1]
            kk += 1

            if(token == hin_tok):

                hindi_2_english_tok = eng_tok
                return hindi_2_english_tok
            else:
                return 0


def hinglish_2_hindi(token, h2h_list):

    jj = 0
    
    for ii in h2h_list:
        
        if(jj < len(h2h_list) - 1):
            
            hinglish_tok = h2h_list[jj][0]
            hin_tok = h2h_list[jj][1]
            jj += 1
            
            if(token == hinglish_tok):

                translate_tok = hin_tok
                return translate_tok
            else:
                return 0

def hindi_2_english_list(h2e_list):

    with open('h2e.csv', 'r') as f:

        reader = csv.reader(f)
        h2e_list = list(reader)

    return h2e_list


def hinglish_2_hindi_list(h2h_list):

    with open('h2h.txt', 'r') as h2h:
        for line in h2h:
            word = line.split()
            h2h_list.append(word)
    
    return h2h_list


def _google_hindi_2_english_(h2e_dict):

    with open('h2e.csv', 'r') as f:
        reader = csv.reader(f)
        h2e_dict = list(reader)

    return h2e_dict

def _google_english_2_hindi_(e2h_dict):

    with open('e2h.csv', 'r') as f:
        reader = csv.reader(f)
        e2h_dict = list(reader)

    return e2h_dict