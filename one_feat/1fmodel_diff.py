import csv
import json

from ...New import features
from ...New import sets
from ..compute import compute_same_d
from ...New import func
from ...New import diction


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
    pos_set = sets.get_pos_set()
    neg_set = sets.get_neg_set()
    neu_set = sets.get_neu_set()

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




    print("Preparing Lists........")
    hindi_2_english_list(h2e_list)
    hinglish_2_hindi_list(h2h_list)
    print("Done!!!!")
    print("............................................")




    print("Training in process, Sit back and relax........")
    with open('../train.json') as json_data:

        d = json.load(json_data)

    column_headers = ['score', 'value']

    with open('var_compute.csv', 'w') as csvFile:

        writer = csv.writer(csvFile)
        writer.writerow(column_headers)

        for each in d:

            print("..", i, "..")

            sentence = each["text"]
            senti_value = each["sentiment"]
            word_id = each["lang_tagged_text"]
            word_id = word_id.replace(" ", "")
            word_id = word_id.lower()
            tokens = features.build_vocab(sentence)

            sent_score = 0
            
            for token in tokens:
                    
                if token in pos_set:

                    sent_score += 30
                    continue
                        
                if token in neu_set:

                    sent_score += 20
                    continue

                if token in neg_set:

                    sent_score += 10
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

                                token = func.spell_correct(token)
                                polarity = func.get_senti(token)
                                sent_score = compute_same_d.compute_score(polarity, sent_score)

                            elif(check == 'h'):

                                hinglish_2_hindi_tok = diction.hinglish_2_hindi(token, h2h_list)

                                if(hinglish_2_hindi_tok != 0):

                                    final_english_tok = diction.hindi_2_english(hinglish_2_hindi_tok, h2e_list)

                                    if(final_english_tok != 0):

                                        polarity = func.get_senti(final_english_tok)
                                        sent_score = compute_same_d.compute_score(polarity, sent_score)

                                    else:

                                        diction._google_hindi_2_english_(h2e_dict)
                                        final_english_tok = diction.google_hindi_2_english(hinglish_2_hindi_tok, h2e_dict)

                                        if(final_english_tok != 0):

                                            polarity = func.get_senti(final_english_tok)
                                            sent_score = compute_same_d.compute_score(polarity, sent_score)

                                        else:
                                            
                                            final_english_tok = func.trans_hin_2_eng(hinglish_2_hindi_tok)
                                            polarity = func.get_senti(final_english_tok)
                                            sent_score = compute_same_d.compute_score(polarity, sent_score)

                                else:

                                    hinglish_2_hindi_tok = func.trans_eng_2_hin(token)

                                    final_english_tok = diction.hindi_2_english(hinglish_2_hindi_tok, h2e_list)

                                    if(final_english_tok != 0):

                                        polarity = func.get_senti(final_english_tok)
                                        sent_score = compute_same_d.compute_score(polarity, sent_score)
                                    
                                    else:

                                        diction._google_hindi_2_english_(h2e_dict)
                                        final_english_tok = diction.google_hindi_2_english(hinglish_2_hindi_tok, h2e_dict)

                                        if(final_english_tok != 0):

                                            polarity = func.get_senti(final_english_tok)
                                            sent_score = compute_same_d.compute_score(polarity, sent_score)

                                        else:

                                            diction._google_english_2_hindi_(e2h_dict)
                                            final_english_tok = diction.google_english_2_hindi(hinglish_2_hindi_tok, h2e_dict)

                                            if(final_english_tok != 0):

                                                polarity = func.get_senti(final_english_tok)
                                                sent_score = compute_same_d.compute_score(polarity, sent_score)

                                            else:

                                                final_english_tok = func.trans_hin_2_eng(hinglish_2_hindi_tok)
                                                polarity = func.get_senti(final_english_tok)
                                                sent_score = compute_same_d.compute_score(polarity, sent_score)


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
                    
 
            row.append(sent_score)
            row.append(senti_value)
                
            writer.writerow(row)
            row = []
            i += 1

print("Done!!!! Now Run accuracy.py")