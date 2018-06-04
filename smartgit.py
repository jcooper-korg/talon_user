# Talon voice commands for SmartGit
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Key, Context

ctx = Context('smartgit', bundle='com.syntevo.smartgit')
ctx.keymap({
    'commit changes': Key('cmd-k'),
	'pull it': Key('cmd-p'),
	'push it': Key('cmd-u'),
  })
