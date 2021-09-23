def card_score(cards):

    if not isinstance(cards, str):
        raise ValueError(f"The 'cards' parameter must be a string, got: {cards}")
    if len(cards.strip()) < 2:
        raise ValueError(f"The 'cards' parameter needs to be >= 2, got: {cards}" )

    numbers = [c for c in cards if c in "23456789"]
    faces = [c for c in cards if c in "JQK"]
    n_aces = [1 for c in cards if c == "A"]
    score = sum([int(i) for i in numbers]) + len(faces) * 10

    for _ in n_aces:
        score += 1 if score + 11 > 21 else 11
        
    return score if score <= 21 else 0