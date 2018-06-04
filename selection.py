# Talon voice commands for selection
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Context, Key

ctx = Context('selection')

ctx.keymap({
	'(shreepway | select to top | sell to top)': Key('cmd-shift-up'),
    '(shroomway | select to end | sell to end | sell to bottom)': Key('cmd-shift-down'),
    '(shreep | select up | select line up | sell up | shift up)': Key('shift-up'),
    '(shroom | select down | select line down | sell down | shift down)': Key('shift-down'),
    '(lecksy | select line left | sell line left)': Key('cmd-shift-left'),
    '(ricksy | select line right | sell line right)': Key('cmd-shift-right'),
    '(scram | select word left | sell word left)': Key('alt-shift-left'),
    '(scrish | select word right | sell word right)': Key('alt-shift-right'),
    '(schrim | select left | sell left | shift left)': Key('shift-left'),
    '(shrish | select right | sell right | shift right)': Key('shift-right'),
})
