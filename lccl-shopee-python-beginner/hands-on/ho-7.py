

def create_deck():
    values = list(range(2,10)) + ['T','J','Q','K','A']
    suits = ['s', 'h', 'd', 'c']
    deck = []

    for s in suits:
        for v in values:
            deck.append(f'{v}s')
    return deck


print(create_deck())