# from https://github.com/talonvoice/examples
# jsc various modificiations as indicated

from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

alpha_alt = 'arch brov char dell etch fomp goof hark ice jinx koop lug mowsh nerb ork pooch quosh rosh sun teak unks verge womp trex yang zooch'.split()
#alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
alpha.update({'ship %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})
alpha.update({'sky %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})		# jsc added

alpha.update({'control %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'command %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'command shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in alnum})

mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
	
	# jsc add remapping
    'et cetera': 'etc',
    'pram': 'param',
    'prams': 'params',
    'end if' : 'endif',
	'multi-' : 'multi',
	'polly' : 'poly',
	'numb' : 'num',
	'portamento' : 'portamento', 
}
punctuation = set('.,-!?')

def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)).lower())

def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    'camel':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'snake':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'smash':  (True,  lambda i, word, _: word),
    # spinal or kebab?
    'kebab':  (True,  lambda i, word, _: word if i == 0 else '-'+word),
    # 'sentence':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    'allcaps': (False, lambda i, word, _: word.upper()),
    'dubstring': (False, surround('"')),
    'string': (False, surround("'")),
    'padded': (False, surround(" ")),
    'rot-thirteen':  (False, rot13),

	# jsc added these:
	'criffed': (True, lambda i, word, _: word.capitalize()),
	'cram': (True,  lambda i, word, _: word.lower() if i == 0 else word.capitalize()),
	'spine': (True,  lambda i, word, _: word if i == 0 else '-'+word),
	'yellsnik':  (True,  lambda i, word, _: word.upper() if i == 0 else '_'+word.upper()),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)
    
ctx = Context('input')

keymap = {}
keymap.update(alpha)
keymap.update({
    'phrase <dgndictation> [over]': text,

    'sentence [<dgndictation>] [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'more <dgndictation> [over]': [' ', text],
    'word <dgnwords>': word,

    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    # jsc moved tab/arrow-keys to navigation.py

    'delete': Key('backspace'),

    'slap': [Key('cmd-right enter')],
    'enter': Key('enter'),
    'escape': Key('esc'),
    'question [mark]': '?',
    'tilde': '~',
    '(bang | exclamation point)': '!',
    'dollar [sign]': '$',
    'downscore': '_',
    '(semi | semicolon)': ';',
    'colon': ':',
    '(square | left square [bracket])': '[', '(rsquare | are square | right square [bracket])': ']',
    '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
    '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
    '(angle | left angle | less than)': '<', '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | hash [sign] | octo | thorpe | number sign)': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    'pipe': '|',

    '(dubquote | double quote)': '"',
    'quote': "'",
    'triple quote': "'''",
    '(dot | period)': '.',
    'comma': ',',
    'space': ' ',
    '[forward] slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot)': '..',
    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    'run get bisect': 'git bisect ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': 'git commit ',
    'run get diff': 'git diff ',
    'run get fetch': 'git fetch ',
    'run get grep': 'git grep ',
    'run get in it': 'git init ',
    'run get log': 'git log ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    'run get rebase': 'git rebase ',
    'run get reset': 'git reset ',
    'run get show': 'git show ',
    'run get status': 'git status ',
    'run get tag': 'git tag ',
    'run (them | vim)': 'vim ',
    'run L S': 'ls\n',
    'dot pie': '.py',
    'run make': 'make\n',
    'run jobs': 'jobs\n',

    'const': 'const ',
    'static': 'static ',
    'tip pent': 'int ',
    'tip char': 'char ',
    'tip byte': 'byte ',
    'tip pent 64': 'int64_t ',
    'tip you went 64': 'uint64_t ',
    'tip pent 32': 'int32_t ',
    'tip you went 32': 'uint32_t ',
    'tip pent 16': 'int16_t ',
    'tip you went 16': 'uint16_t ',
    'tip pent 8': 'int8_t ',
    'tip you went 8': 'uint8_t ',
#    'tip size': 'size_t',				# jsc removed
    'tip float': 'float ',
    'tip double': 'double ',

    'args': ['()', Key('left')],
	'brax': ['[]', Key('left')],			# jsc renamed from index to brax
    'block': [' {}', Key('left enter enter up tab')],
    'empty array': '[]',
    'empty dict': '{}',

    'state (def | deaf | deft)': 'def ',
    'state else if': 'elif ',
    'state if': 'if ',
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state for': 'for ',
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    'state goto': 'goto ',
    'state import': 'import ',
    'state class': 'class ',

    'state include': '#include ',
    'state include system': ['#include <>', Key('left')],
    'state include local': ['#include ""', Key('left')],
    'state type deaf': 'typedef ',
    'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    'comment see': '// ',
    'comment py': '# ',

    'word queue': 'queue',
    'word eye': 'eye',
    'word bson': 'bson',
    'word iter': 'iter',
    'word no': 'NULL',
    'word cmd': 'cmd',
    'word dup': 'dup',
    'word streak': ['streq()', Key('left')],
    'word printf': 'printf',
    'word (dickt | dictionary)': 'dict',
    'word shell': 'shell',

    'word lunixbochs': 'lunixbochs',
    'word talon': 'talon',
    'word Point2d': 'Point2d',
    'word Point3d': 'Point3d',
    'title Point': 'Point',
    'word angle': 'angle',

    'dunder in it': '__init__',
    'self taught': 'self.',
    'dickt in it': ['{}', Key('left')],
    'list in it': ['[]', Key('left')],
    'string utf8': "'utf8'",
    'state past': 'pass',

    'equals': '=',
    '(minus | dash)': '-',
    'plus': '+',
    'arrow': '->',
#    'call': '()',			# jsc removed this
    'indirect': '&',
    'dereference': '*',
    'op equals': ' = ',
    'op (minus | subtract)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | multiply)': ' * ',
    'op divide': ' / ',
    'op mod': ' % ',
    '[op] (minus | subtract) equals': ' -= ',
    '[op] (plus | add) equals': ' += ',
    '[op] (times | multiply) equals': ' *= ',
    '[op] divide equals': ' /= ',
    '[op] mod equals': ' %= ',

    '(op | is) greater [than]': ' > ',
    '(op | is) less [than]': ' < ',
    '(op | is) equal': ' == ',
    '(op | is) not equal': ' != ',
    '(op | is) greater [than] or equal': ' >= ',
    '(op | is) less [than] or equal': ' <= ',
    '(op (power | exponent) | to the power [of])': ' ** ',
    'op and': ' && ',
    'op or': ' || ',
    '[op] (logical | bitwise) and': ' & ',
    '[op] (logical | bitwise) or': ' | ',
    '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    '(op | logical | bitwise) and equals': ' &= ',
    '(op | logical | bitwise) or equals': ' |= ',
    '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    'shebang bash': '#!/bin/bash -u\n',

    'new window': Key('cmd-n'),
    'next window': Key('cmd-`'),
    '(last | preev) window': Key('cmd-shift-`'),	# jsc added prev
    'next app': Key('cmd-tab'),
    '(last | preev) app': Key('cmd-shift-tab'),		# jsc added prev
    'next tab': Key('ctrl-tab'),
    'new tab': Key('cmd-t'),
    '(last | preev) tab': Key('ctrl-shift-tab'),	# jsc added prev

    'next space': Key('cmd-alt-ctrl-right'),
    '(last | preev) space': Key('cmd-alt-ctrl-left'),

    'scroll down': [Key('down')] * 30,
    'scroll up': [Key('up')] * 30,
})

#---- jsc added the following
def select_text_to_left_of_cursor(m, cursorKey, clipboardSelectKey='shift-home'):
	key = join_words(parse_words(m)).lower()
	with clip.capture() as clipboardText:
		press(clipboardSelectKey, wait=20000)
		press('cmd-c', wait=20000)
		press('right', wait=20000)
	searchText = clipboardText.get().lower()
	result = searchText.rfind(key)
	if result == -1:
		return False
	# cursor over to the found key text and select the matching text
	for i in range(result, len(searchText) - len(key)):
		press(cursorKey, wait=0)
	for i in range(0, len(key)):
		press('shift-left', wait=0)
	return True

def select_text_to_right_of_cursor(m, cursorKey, clipboardSelectKey='shift-end'):
	key = join_words(parse_words(m)).lower()
	with clip.capture() as clipboardText:
		press(clipboardSelectKey, wait=20000)
		press('cmd-c', wait=20000)
		press('left', wait=20000)
	searchText = clipboardText.get().lower()
	result = searchText.find(key)
	if result == -1:
		return False
	# cursor over to the found key text and select the matching text
	for i in range(0, result):
		press(cursorKey, wait=0)
	for i in range(0, len(key)):
		press('shift-right', wait=0)
	return True

def select_text_on_same_line(m):
	key = join_words(parse_words(m)).lower()
	# first check to the left of the cursor
	if select_text_to_left_of_cursor(m, cursorKey='left', clipboardSelectKey='shift-ctrl-a') == False:
		# if nothing found, then check to the right of the cursor
		select_text_to_right_of_cursor(m, cursorKey='right', clipboardSelectKey='shift-ctrl-e')

keymap.update({
    'say <dgndictation> [over]': text,
    'cap <dgndictation> [over]': sentence_text,
    '(find text | marco) <dgndictation> [over]': [Key("cmd-f"), text, Key("enter")],
    '(find text | marco)': Key("cmd-f"),
    '(find selected text | find selection | sell find)': Key("cmd-e cmd-f enter"),
    '(find next | marnek)': Key('cmd-g'),
    '(find preev | marpreev)': Key('cmd-shift-g'),
    'set selection': Key('cmd-e'),
    'set replacement': Key('cmd-shift-e'),
    '(replace selected text | replace selection | sell find ace)': Key('cmd-e cmd-alt-f'),
    '(replace text | find ace)': Key('cmd-alt-f'),
    'close window': Key('cmd-w'),
    'quit window': Key('cmd-q'),
    '(crew | find right) <dgndictation> [over]': lambda m: select_text_to_right_of_cursor(m, cursorKey='right'),
    '(selcrew | crew select | sell find right) <dgndictation> [over]': lambda m: select_text_to_right_of_cursor(m, cursorKey='shift-right'),
    '(trail | find left) <dgndictation> [over]': lambda m: select_text_to_left_of_cursor(m, cursorKey='left'),
    '(seltrail | trail select | sell find left) <dgndictation> [over]': lambda m: select_text_to_left_of_cursor(m, cursorKey='shift-left'),
    'kerleck <dgndictation> [over]': select_text_on_same_line,
})


alpha.update({'control shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
alpha.update({'control option %s' % k: Key('ctrl-alt-%s' % v) for k, v in alnum})
alpha.update({'command control %s' % k: Key('cmd-ctrl-%s' % v) for k, v in alnum})
alpha.update({'command option %s' % k: Key('cmd-alt-%s' % v) for k, v in alnum})
alpha.update({'option %s' % k: Key('alt-%s' % v) for k, v in alnum})
alpha.update({'option shift %s' % k: Key('alt-shift-%s' % v) for k, v in alnum})

# this was the Voice Code alphabet:

ctx.keymap(keymap)
