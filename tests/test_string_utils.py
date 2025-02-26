from src.stringutils.py import upper_case, lower_case, palindrome_str, reverse_str

def test_upper_case():
  assert upper_case("really") == "REALLY"
  assert upper_case("nooo") == "NOOO"

def test_lower_case():
  assert lower_case("WOW") == "wow"
  assert lower_case("SERIOUSLY") == "seriously"

def test_palindrome_str():
  assert palindrome_str("level") is True
  assert palindrome_str("mother") is False

def test_reverse_str():
  assert reverse_str("truly") == "ylurt"
  assert reverse_str("nothing") == "gnihton"

