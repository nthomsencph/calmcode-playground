from blackjack.common import card_score
import pytest

@pytest.mark.parametrize("cards,score", [
    ("KQ", 20),
    ("KQ5", 0),
    ("AK", 21),
])
def test_simple_case1(cards, score):
    assert card_score(cards) == score

def test_advanced_case():
    assert card_score("A2222QA") == 20

def test_triple_ace_case():
    assert card_score("AAA") == 13

@pytest.mark.parametrize("cards", [
    "A",
    "",
    "  ",
    122,
    1
])
def test_value_error_is_raised(cards):
    with pytest.raises(ValueError):
        card_score(cards)