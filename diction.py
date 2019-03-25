import csv
import json


def hinglish_to_hindi_list(h2h_list):

    with open('h2h.txt', 'r') as h2h:
        for line in h2h:
            word = line.split()
            h2h_list.append(word)
    return h2h_list


def hindi_to_english_list(h2e_list):

    with open('h2e.csv', 'r') as f:
        reader = csv.reader(f)
        h2e_list = list(reader)
    return h2e_list


def find_hinglish_to_hindi(token, h2h_list):

    jj = 0
    
    for ii in h2h_list:
        
        if(jj < len(h2h_list) - 1):
            
            hinglish_tok = h2h_list[jj][0]
            hin_tok = h2h_list[jj][1]
            jj += 1
            
            if(token == hinglish_tok):

                translate_tok = hin_tok

                return translate_tok
    return 0


def find_hindi_to_english(token, h2e_list):

    kk = 0
    
    for ss in h2e_list:
        
        if(kk < len(h2e_list)):
            
            eng_tok = h2e_list[kk][0]
            hin_tok = h2e_list[kk][1]
            kk += 1

            if(token == hin_tok):

                hindi_2_english_tok = eng_tok
                return hindi_2_english_tok
    return 0

