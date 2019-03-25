import csv
import json
import sys

sys.path.append(0, r'/Users/mac/Downloads/BIT\ 4th\ Semester/Thesis/Models/KNN\ Model/New/compute')

from features import build_vocab

from sets import get_pos_set, get_neu_set, get_neg_set

from compute import sub_compute

from func import trans_eng_2_hin, trans_hin_2_eng, get_senti, spell_correct, get_sub

from diction import google_english_2_hindi, google_hindi_2_english, hindi_2_english, hinglish_2_hindi
from diction import hindi_2_english_list, hinglish_2_hindi_list, _google_hindi_2_english_, _google_english_2_hindi_





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

    pos_set.discard('EMOPOS')
    pos_set.discard('EMONEG')
    pos_set.discard('EMONEU')
    neg_set.discard('EMOPOS')
    neg_set.discard('EMONEG')
    neg_set.discard('EMONEU')
    neu_set.discard('EMOPOS')
    neu_set.discard('EMONEG')
    neu_set.discard('EMONEU')
    pos_set.add('EMOPOS')
    neg_set.add('EMONEG')
    neu_set.add('EMONEU')
    print("Done!!!")
    print("............................................")

    print("Preparing List........")
    hindi_2_english_list(h2e_list)
    hinglish_2_hindi_list(h2h_list)
    print("Done!!!!")
    print("............................................")

    print("Training the Model, Sit back and relax........")

    with open('../train.json') as json_data:

        d = json.load(json_data)

    column_headers = ['pos_score', 'neu_score', 'neg_score', 'sub_score' 'value']

    with open('level_compute.csv', 'w') as csvFile:

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

            pos_score = 0
            neg_score = 0
            neu_score = 0
            pos_sub_score = 0
            neu_sub_score = 0
            neg_sub_score = 0
            
            for token in tokens:
                    
                if token in pos_set:

                    pos_score += 10
                    continue
                        
                if token in neu_set:

                    neu_score += 10
                    continue

                if token in neg_set:

                    neg_score += 10
                    continue
                    
                else:

                    find_pos = token.find('emopos')
                    find_neu = token.find('emoneu')
                    find_neg = token.find('emoneg')

                    if(find_pos == -1 and find_neg == -1 and find_neu == -1):

                        start = word_id.find(token)

                        if(start == -1):
                            continue

                        else:

                            end = start + len(token)
                            check = word_id[end+1]

                            if(check == "e"):

                                token = spell_correct(token)
                                polarity = get_senti(token)
                                theory = get_sub(token)

                                sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)

                            elif(check == 'h'):

                                hinglish_2_hindi_tok = hinglish_2_hindi(token, h2h_list)

                                if(hinglish_2_hindi_tok != 0):

                                    final_english_tok = hindi_2_english(hinglish_2_hindi_tok, h2e_list)

                                    if(final_english_tok != 0):

                                        polarity = get_senti(final_english_tok)
                                        sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)

                                    else:

                                        _google_hindi_2_english_(h2e_dict)
                                        final_english_tok = google_hindi_2_english(hinglish_2_hindi_tok, h2e_dict)

                                        if(final_english_tok != 0):

                                            polarity = get_senti(final_english_tok)
                                            sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)

                                        else:
                                            
                                            final_english_tok = trans_hin_2_eng(hinglish_2_hindi_tok)
                                            polarity = get_senti(final_english_tok)
                                            sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)

                                else:

                                    hinglish_2_hindi_tok = trans_eng_2_hin(token)
                                    final_english_tok = hindi_2_english(hinglish_2_hindi_tok, h2e_list)

                                    if(final_english_tok != 0):

                                        polarity = get_senti(final_english_tok)
                                        sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)
                                    
                                    else:

                                        _google_hindi_2_english_(h2e_dict)
                                        final_english_tok = google_hindi_2_english(hinglish_2_hindi_tok, h2e_dict)

                                        if(final_english_tok != 0):

                                            polarity = get_senti(final_english_tok)
                                            sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)

                                        else:

                                            _google_english_2_hindi_(e2h_dict)
                                            final_english_tok = google_english_2_hindi(hinglish_2_hindi_tok, h2e_dict)

                                            if(final_english_tok != 0):

                                                polarity = get_senti(final_english_tok)
                                                sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)

                                            else:

                                                final_english_tok = trans_hin_2_eng(hinglish_2_hindi)
                                                polarity = get_senti(final_english_tok)
                                                sub_compute.compute_score(polarity, pos_score, neu_score, neg_score, pos_sub_score, neu_sub_score, neg_sub_score, theory)


                    elif(find_pos > 0):

                        if(senti_value == 1):
                            pos_score += 10
                            continue
                        elif(senti_value == 0):
                            neu_score += 10
                        else:
                            neg_score += 10


                    elif(find_neu > 0):
                        if(senti_value == 1):
                            pos_score += 10
                            continue
                        elif(senti_value == 0):
                            neu_score += 10
                        else:
                            neg_score += 10
                
                    else:
                        if(senti_value == 1):
                            pos_score += 10
                            continue
                        elif(senti_value == 0):
                            neu_score += 10
                        else:
                            neg_score += 10
                    
 
            row.append(pos_score)
            row.append(neu_score)
            row.append(neg_score)
            row.append(pos_sub_score)
            row.append(neu_sub_score)
            row.append(neg_sub_score)
            row.append(senti_value)
                
            writer.writerow(row)
            row = []
            i += 1

print("Done! Now Run accuracy.py")