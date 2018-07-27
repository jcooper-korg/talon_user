# Talon voice commands for interacting with the Finder
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Key, Context

ctx = Context('Finder', bundle='com.apple.finder')
ctx.keymap({
    'duplicate': Key('cmd-d'),
	'collapse': Key('cmd-left'),
	'expand': Key('cmd-right'),
	'open': Key('cmd-down'),
	'trash it': Key('cmd-backspace'),
	'show package contents': Key('cmd-alt-o'),
 })
