def sum_points(hand):

    card_score = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    score = 0
    cnt_aces = 0
    for card in hand:
        score += card_score[card.value]
        if card.value == 'A':
            cnt_aces += 1

    if score >= 21 and cnt_aces > 0:
        score = score - cnt_aces*10

    return score
