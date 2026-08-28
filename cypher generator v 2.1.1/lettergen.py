import string
import secrets
extra_symbols = "¶§†¤"
letters = list(string.ascii_uppercase+string.digits)
symbols = list(string.punctuation+extra_symbols)

def choose_letter():
    global letters
    letter = secrets.choice(letters)
    letters.remove(letter)
    return letter

def choose_symbol():
    global symbols
    symbol = secrets.choice(symbols)
    symbols.remove(symbol)
    return symbol

def no_value():
    blank_value = ' '
    return blank_value

def reset_lists():
    global letters, symbols
    letters = list(string.ascii_uppercase+string.digits)
    symbols = list(string.punctuation+extra_symbols)

    
