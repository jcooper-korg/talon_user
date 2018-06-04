# from https://github.com/JonathanNickerson/talon_voice_user_scripts
# jsc removed selection commands to new file selection.py

from talon.voice import Context, Key

ctx = Context('navigation')

keymap = {
    # Requires activation of System Preferences -> Shortcuts -> Input Sources
    # -> "Select the previous input source"
    'change language': Key('ctrl-space'),

    # Application navigation
    'swick': Key('cmd-tab'),
    'totch': Key('cmd-w'),
    'chom quosh': Key('cmd-q'),
    'new window': Key('cmd-n'),
    '(next window | gibby)': Key('cmd-`'),
    '(last window | shibby)': Key('cmd-shift-`'),
    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    # Following three commands should be application specific
    #'(baxley | go back)': Key('cmd-alt-left'),
    #'(fourthly | go forward)': Key('cmd-alt-right'),
    # '(new tab | peach)': Key('cmd-t'),

    # deleting
    '(snipline | delete line)': Key('cmd-right cmd-backspace'),
    'steffi': Key('alt-ctrl-backspace'),
    'stippy': Key('alt-ctrl-delete'),
    '(carmex | delete word left | dell word left)': Key('alt-backspace'),
    '(kite | delete word right | dell word right)': Key('alt-delete'),
    'snipple': Key('cmd-shift-left delete'),
    'snipper': Key('cmd-shift-right delete'),
    'slurp': Key('backspace delete'),
    'slurpies': Key('alt-backspace alt-delete'),

    # moving
    '(tab | tarp)': Key('tab'),
    'tarsh': Key('shift-tab'),
    'slap': [Key('cmd-right enter')],
    'shocker': [Key('cmd-left enter up')],
    '(partial word left | wonkrim)': Key('alt-ctrl-left'),
    '(partial word right | wonkrish)': Key('alt-ctrl-right'),
    '(word left | fame)': Key('alt-left'),
    '(word right | fish)': Key('alt-right'),
    'ricky': Key('cmd-right'),
    'lefty': Key('cmd-left'),
    '(left | crimp)': Key('left'),
    '(right | chris)': Key('right'),
    '(up | jeep)': Key('up'),
    '(down | dune | doom)':  Key('down'),

    'scroll down': [Key('down')] * 30,
    '(doomway | scroll way down)': Key('cmd-down'),
    'scroll up': [Key('up')] * 30,
    '(jeepway | scroll way up)': Key('cmd-up'),
}

ctx.keymap(keymap)
