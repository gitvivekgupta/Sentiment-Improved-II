import csv
import json
from textblob import TextBlob
from nltk.corpus import wordnet
from features import build_vocab
from googletrans import Translator
from spellchecker import SpellChecker
from multiprocessing import Process, Queue

neu_features = "neu_features.txt"
neu_feature_file = open(neu_features, "r")

neg_features = "neg_features.txt"
neg_feature_file = open(neg_features, "r")

pos_features = "pos_features.txt"
pos_feature_file = open(pos_features, "r")

neu_set = set()
neu_set_c = set()

neg_set = set()
neg_set_c = set()

pos_set = set()
pos_set_c = set()
pos_set_cc = set()

for neu_word in neu_feature_file:

        neu_set.add(neu_word)
        neu_set_c.add(neu_word)

for neg_word in neg_feature_file:

        neg_set.add(neg_word)
        neg_set_c.add(neg_word)

for pos_word in pos_feature_file:

        pos_set.add(pos_word)
        pos_set_c.add(pos_word)
        pos_set_cc.add(pos_word)


pos_set.difference_update(neg_set)
pos_set.difference_update(neu_set)

neg_set.difference_update(pos_set_c)
neg_set.difference_update(neu_set)

neu_set.difference_update(neg_set_c)
neu_set.difference_update(pos_set_cc)

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

print("Training the Model, Sit Back and Relax....")

row = []
i = 1

with open('train.json') as json_data:

    d = json.load(json_data)

column_headers = ['pos_score', 'neu_score', 'neg_score', 'sub_score', 'value']

with open('data.csv', 'w') as csvFile:

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
        neu_score = 0
        neg_score = 0
        sub_score = 0
            
        for token in tokens:
                    
            if token in pos_set:

                pos_score += 30
                continue
                        
            if token in neu_set:

                neu_score += 20
                continue

            if token in neg_set:
                
                neg_score += 10
                continue
                    
            else:

                start = word_id.find(token)

                if(start == -1):
                    continue

                else:
                
                    end = start + len(token)
                    check = word_id[end+1]

                    if(check == "e"):

                        spell = SpellChecker()

                        if(spell.known(token)):

                            testimonial = TextBlob(token)
                            polarity = testimonial.sentiment.polarity
                            theory = testimonial.sentiment.subjectivity

                            if(polarity >= .2):
                                pos_score += 30
                                sub_score += theory

                            elif(polarity > -.2 and polarity < .2):
                                neu_score += 20
                                sub_score += theory

                            else:
                                neg_score += 10
                                sub_score += theory

                        else:

                            new_token = spell.correction(token)

                            testimonial = TextBlob(new_token)
                            polarity = testimonial.sentiment.polarity
                            theory = testimonial.sentiment.subjectivity

                            if(polarity >= .2):
                                pos_score += 30
                                sub_score += theory

                            elif(polarity > -.2 and polarity < .2):
                                neu_score += 20
                                sub_score += theory

                            else:
                                neg_score += 10
                                sub_score += theory
                    
                    elif(check == 'h'):
                        
                        translator = Translator()
                        trans_token = translator.translate(token, dest='en', src='hi')
                        trans_token = trans_token.text

                        spell = SpellChecker()
                        trans_token = spell.correction(trans_token)

                        testimonial = TextBlob(trans_token)
                        polarity = testimonial.sentiment.polarity
                        theory = testimonial.sentiment.subjectivity

                        if(polarity >= .2):
                            pos_score += 30
                            sub_score += theory

                        elif(polarity > -.2 and polarity < .2):
                            pos_score += 20
                            sub_score += theory

                        else:
                            neg_score += 10
                            sub_score += theory

                    else:
                        continue
 
        row.append(pos_score)
        row.append(neu_score)
        row.append(neg_score)
        row.append(sub_score)
        row.append(senti_value)
                
        writer.writerow(row)
        row = []
        i += 1

print("Done!!! Now run accuracy.py")