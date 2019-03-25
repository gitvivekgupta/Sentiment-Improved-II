

def pos_compute_score(sent_score):

    sent_score += 30
    return sent_score

def neu_compute_score(sent_score):

    sent_score += 20
    return sent_score

def neg_compute_score(sent_score):

    sent_score += 10
    return sent_score


def compute_score(polarity, sent_score):

    if(polarity >= .2):
        sent_score += 30
        
    elif(polarity > -.2 and polarity < .2):
        sent_score += 20
        
    else:
        sent_score += 10
    return sent_score
