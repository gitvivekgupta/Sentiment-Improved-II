import csv
import json

compute = r'/Users/mac/Downloads/BIT\ 4th\ Semester/Thesis/Models/KNN\ Model/New/compute'

from features import build_vocab
from sets import get_pos_set, get_neu_set, get_neg_set
from compute.sent_score_same import pos_compute_score, neu_compute_score, neg_compute_score, compute_score
from func import goog_trans_english_to_hindi, goog_trans_hindi_to_english, get_senti, spell_correct
from diction import hindi_to_english_list, hinglish_to_hindi_list, find_hindi_to_english, find_hinglish_to_hindi


if __name__ == "__main__":
    
    h2h_list = []
    h2e_list = []
    h2e_dict = []
    e2h_dict = []
    row = []
    i = 1
    flag = 0
    found = 0
    not_found = 1


    print("Preparing sets.......")
    pos_set = get_pos_set()
    neg_set = get_neg_set()
    neu_set = get_neu_set()

    pos_set.discard('emopos')
    pos_set.discard('emoneg')
    pos_set.discard('emoneu')

    neg_set.discard('emopos')
    neg_set.discard('emoneg')
    neg_set.discard('emoneu')

    neu_set.discard('emopos')
    neu_set.discard('emoneg')
    neu_set.discard('EMONEU')

    pos_set.add('emopos')
    neg_set.add('emoneg')
    neu_set.add('emoneu')
    print("Done!!!")
    print("............................................")




    print("Preparing Lists........")
    h2h_list_returned = hinglish_to_hindi_list(h2h_list)
    h2e_list_returned = hindi_to_english_list(h2e_list)
    print("Done!!!!")
    print("............................................")




    print("Training in process, Sit back and relax........")

    with open('../train.json') as json_data:

        d = json.load(json_data)

    column_headers = ['score', 'value']

    with open('var_score.csv', 'w') as csvFile:

        writer = csv.writer(csvFile)
        writer.writerow(column_headers)

        for each in d:

            print("..", i, "..")

            sentence = each["text"]
            senti_value = each["sentiment"]
            word_id = each["lang_tagged_text"]
            word_id = word_id.replace(" ", "")
            word_id = word_id.lower()
            tokens = build_vocab(sentence)

            sent_score = 0
            
            for token in tokens:
                    
                if token in pos_set:

                    sent_score = pos_compute_score(sent_score)
                    continue
                        
                if token in neu_set:

                    sent_score = neu_compute_score(sent_score)
                    continue

                if token in neg_set:

                    sent_score = neg_compute_score(sent_score)
                    continue
                    
                else:

                    start = word_id.find(token)

                    if(start == -1):

                        final_hindi_tok = find_hinglish_to_hindi(token, h2h_list_returned)

                        if(final_hindi_tok != 0):

                            final_english_tok = find_hindi_to_english(final_hindi_tok, h2e_list_returned)

                            if(final_english_tok != 0):

                                final_english_tok = spell_correct(final_english_tok)
                                polarity = get_senti(final_english_tok)
                                sent_score = compute_score(polarity, sent_score)
                                continue

                            else:

                                trans_english_tok = goog_trans_hindi_to_english(final_hindi_tok)
                                final_english_tok = spell_correct(trans_english_tok)
                                polarity = get_senti(final_english_tok)
                                sent_score = compute_score(polarity, sent_score)
                                continue

                        else:
                            continue

                    else:

                        end = start + len(token)
                        check = word_id[end+1]

                        if(check == "e"):

                            final_english_tok = spell_correct(token)
                            polarity = get_senti(final_english_tok)
                            sent_score = compute_score(polarity, sent_score)

                        elif(check == 'h'):

                            final_hindi_tok = find_hinglish_to_hindi(token, h2h_list_returned)

                            if(final_hindi_tok != 0):

                                final_english_tok = find_hindi_to_english(final_hindi_tok, h2e_list_returned)

                                if(final_english_tok != 0):

                                    polarity = get_senti(final_english_tok)
                                    sent_score = compute_score(polarity, sent_score)

                                else:
                                
                                    trans_english_tok = goog_trans_hindi_to_english(final_hindi_tok)
                                    final_english_tok = spell_correct(trans_english_tok)
                                    polarity = get_senti(final_english_tok)
                                    sent_score = compute_score(polarity, sent_score)

                            else:
                                
                                trans_hindi_tok = goog_trans_english_to_hindi(token)
                                trans_english_tok = goog_trans_hindi_to_english(trans_hindi_tok)
                                final_english_tok = spell_correct(trans_english_tok)
                                polarity = get_senti(final_english_tok)
                                sent_score = compute_score(polarity, sent_score)

                        else:
                            continue

 
            row.append(sent_score)
            row.append(senti_value)
                
            writer.writerow(row)
            row = []
            i += 1

print("Done!!!! Now Run accuracy.py")