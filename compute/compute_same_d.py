
def compute_score(polarity, sent_score):

    if(polarity >= .2):
        sent_score += 30
        
    elif(polarity > -.2 and polarity < .2):
        sent_score += 20
        
    else:
        sent_score += 10

    return sent_score