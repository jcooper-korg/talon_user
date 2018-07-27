# Talon voice commands for Xcode
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Key, Context

ctx = Context('xcode', bundle='com.apple.dt.Xcode')

ctx.keymap({
    '(build it | chom brov)': Key('cmd-b'),
    '(stop it | chom peer)': Key('cmd-.'),
    '(run it | chom rosh)': Key('cmd-r'),
	'go back': Key('cmd-ctrl-left'),
	'go fore': Key('cmd-ctrl-right'),
	'find in proj': Key('cmd-shift-f'),
	'(sell find in proj | find selection in project)': Key('cmd-e cmd-shift-f enter'),
	'(sell find ace in proj | replace selection in project)': Key('cmd-e cmd-shift-alt-f'),
	'split window': Key('cmd-alt-enter'),
	'show editor': Key('cmd-enter'),
	'(show | hide) debug': Key('cmd-shift-y'),
	'(show | hide) navigator': Key('cmd-0'),
	'show call hierarchy': Key('cmd-ctrl-shift-h'),
	'show warnings': Key('cmd-4'),
	'show diffs': Key('cmd-alt-shift-enter'),
	'(next counterpart | show header | switcher)': Key('cmd-ctrl-down'),
	'prev counterpart': Key('cmd-ctrl-up'),
	'toggle comment': Key('cmd-/'),
	'toggle breakpoint': Key('cmd-\\'),
	'toggle all breakpoints': Key('cmd-y'),
	'move line up': Key('cmd-alt-['),
	'move line down': Key('cmd-alt-]'),
	'go deafen': Key('cmd-ctrl-j'),
	'edit scheme': Key('cmd-shift-,'),
	'quick open': Key('cmd-shift-o'),
    'jolt': Key('ctrl-a shift-down cmd-c down cmd-v' ),
	'comm skoosh': '// ',
	'comm line': ['//------------------------------------------------------------------------------', Key('enter')],
	'(select partial word left | sell partial word left | sell partial left | sell sub left)': Key('shift-ctrl-left'),
    '(select partial word right | sell partial word right | sell partial right | sell sub right)': Key('shift-ctrl-right'),

	# the following require custom key bindings in xcode preferences
    '(partial word left | subword left | wonkrim)': Key('alt-ctrl-left'),
    '(partial word right | subword right | wonkrish)': Key('alt-ctrl-right'),

	'show blame for line': Key('cmd-alt-ctrl-b'),
	'(snipline | delete line)': Key('cmd-alt-ctrl-shift-backspace'),
})
