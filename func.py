import csv
import json
from textblob import TextBlob
from google.cloud import translate
from spellchecker import SpellChecker

    

def trans_hin_2_eng(token):

    translate_client = translate.Client()
    translation = translate_client.translate(token, source_language='hi')
    converted_tok = translation['translatedText']

    to_write = [token, converted_tok]

    with open('h2edict.csv', 'a') as h2ecsv:

        writer = csv.writer(h2ecsv)
        writer.writerow(to_write)

    h2ecsv.close()

    return converted_tok


def trans_eng_2_hin(token):

    translate_client = translate.Client()
    target = 'hi'
    translation = translate_client.translate(token, source_language='en', target_language=target)
    converted_tok = translation['translatedText']

    to_write = [token, converted_tok]

    with open('e2hdict.csv', 'a') as e2hcsv:

        writer = csv.writer(e2hcsv)
        writer.writerow(to_write)

    e2hcsv.close()

    return converted_tok


def get_senti(token):

    testimonial = TextBlob(token)
    polarity = testimonial.sentiment.polarity

    return polarity


def get_sub(token):

    testimonial = TextBlob(token)
    theory = testimonial.sentiment.subjectivity

    return theory


def spell_correct(token):

    spell = SpellChecker()

    if(spell.known(token)):
        return token
    else:
        spell_correct_tok = spell.correction(token)

    return spell_correct_tok


