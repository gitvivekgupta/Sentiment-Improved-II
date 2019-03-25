from google.cloud import translate
from spellchecker import SpellChecker
from textblob import TextBlob

def get_senti(token):

    testimonial = TextBlob(token)
    polarity = testimonial.sentiment.polarity
    return polarity


def goog_trans_hindi_to_english(token):

    translate_client = translate.Client()
    translation = translate_client.translate(token, source_language='hi')
    converted_tok = translation['translatedText']
    return converted_tok


def goog_trans_english_to_hindi(token):

    translate_client = translate.Client()
    target = 'hi'
    translation = translate_client.translate(token, source_language='en', target_language=target)
    converted_tok = translation['translatedText']
    return converted_tok


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


