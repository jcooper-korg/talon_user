# from https://github.com/JonathanNickerson/talon_voice_user_scripts
# jsc added C and C++ keywords, etc.  simplified context for now

from talon.voice import Context, Key

#languages = ['.php', '.py', '.java', '.yml', '.json']
#bundles = ['com.postmanlabs.mac']
#
#ctx = Context('code', func=lambda app, win:
#              any(app.bundle == b for b in bundles)
#              or any(win.doc.endswith(l) for l in languages)
#              )

ctx = Context('code')
keymap = {
    'sinker': [Key('cmd-right ;')],

    '(args | prex)': ['()', Key('left')],
    'angler': ['<>', Key('left')],
    '(block | kirblock)': ['{}', Key('left enter')],
    'args-block': ['(', Key('enter')],
    'brax-block': ['[', Key('enter')],

    'coalshock': [':', Key('enter')],
    'coal twice': '::',
    'ellipsis': '...',
    'mintwice': '--',
    'plustwice': '++',

    '(indirect | reference)': '&',
    '([is] equal to | longqual)': ' == ',
    '([is] not equal to | banquall)': ' != ',
    'trickle': ' === ',
    '(ranqual | nockle)': ' !== ',
    '(call | prekris)': '()',

    '(index | brax)': ['[]', Key('left')],
    '(empty dict | kirk)': ['{}', Key('left')],

    '(empty array | brackers)': '[]',
    'empty dict': '{}',
	
	# jsc added spaces around all these
    'minquall': ' -= ',
    'pluqual': ' += ',
    'starqual': ' *= ',
    'lessqual': ' <= ',
    'grayqual': ' >= ',
    'equeft': ' = ',
    'daplush': ' + ',

    '(arrow | lambo)': '->',
    'shrocket': ' => ',

	'state if': ['if ()', Key('left')],
    'state else': ['else {}', Key('left enter')],
    'state else if': ['else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state for each': ['foreach ()', Key('left')],
    'state switch': ['switch ()', Key('left')],

    'const': 'const ',
    'static': 'static ',
    'tip pent': 'int ',
	
    'word no': 'null',
    'word printf': 'printf',
    'word define': 'def ',
    'word import': 'import ',

    # jsc added: C preprocessor, C++ keywords
    'pragma once': '#pragma once',
    '(pound include | hashtag include | see include)': ['#include ""', Key('left')],
    '(pound angle include | hashtag angle include | see angle include)': ['#include <>', Key('left')],
    'pound define': '#define ',
    'pound if': '#if ',
    'pound else': '#else',
    'pound endif': '#endif',
    'pound if block': ['#if ', Key('enter'), '#endif', Key('enter up up cmd-right')],
    'pound if else block': ['#if ', Key('enter'), '#else ', Key('enter'), '#endif', Key('enter up up up cmd-right')],
	'class': 'class ',
	'struct': 'struct ',
	'public': 'public',
	'protected': 'protected',
	'private': 'private',
    'word no pointer': 'nullptr',

    '(coif | dubquote block | double quote block)' : ['""', Key('left')],
    '(posh | quote block)' : ["''", Key('left')],


}

ctx.keymap(keymap)
