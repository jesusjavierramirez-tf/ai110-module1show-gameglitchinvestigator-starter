from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_parse_guess_rejects_blank_input():
    ok, guess, error = parse_guess("   ")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_score_only_changes_on_win():
    assert update_score(0, "Too High", 1) == 0
    assert update_score(0, "Win", 1) == 100
