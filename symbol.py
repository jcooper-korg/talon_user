# from https://github.com/JonathanNickerson/talon_voice_user_scripts/blob/master/symbol.py

from talon.voice import Context, Key

ctx = Context('symbol')

keymap = {
    '(escape | randall)': Key('esc'),
    '(question [mark] | questo)': '?',
    '(minus | dash)': '-',
    'plus': '+',
    'tilde': '~',
    '(bang | exclamation point | clamor)': '!',
    '(dollar [sign] | dolly)': '$',
    '(downscore | crunder | underscore)': '_',
    '(semi | semicolon | sunk)': ';',
    'colon': ':',
	
    '(square | left square [bracket] | brackorp)': '[',
    '(rsquare | are square | right square [bracket] | brackose)': ']',
    '(paren | left paren | pracorp)': '(',
    '(rparen | are paren | right paren | pracose)': ')',
    '(brace | left brace | kirksorp)': '{',
    '(rbrace | are brace | right brace | kirkos)': '}',
    '(angle | left angle | less than)': '<',
    '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | hash [sign] | octo | thorpe | number sign)': '#',
    '(percent [sign] | percy)': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    '(pipe | spike)': '|',

    '(dubquote | double quote | quatches)': '"',
    '(quote | quatchet)': "'",
    'triple quote': "'''",
    '(dot | period)': '.',
    'comma': ',',
    'swipe': ', ',
    'coalgap': ': ',
    '(space | skoosh)': ' ',
    '[forward] slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot | doodle)': '..',
    '(enter | shock)': Key('enter'),
    '(delete | junk)': Key('backspace'),
    'spunk': Key('delete'),

    'equals': '=',
}

ctx.keymap(keymap)
