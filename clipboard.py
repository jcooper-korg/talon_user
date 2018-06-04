# Talon voice commands for interacting with macOS Finder
# John S. Cooper  jcooper@korgrd.com

from talon.voice import ctrl, Key, Context

ctx = Context('clipboard')

def double_click(m):
   x, y = ctrl.mouse_pos()
   ctrl.mouse_click(x, y, button=0, times=2, wait=16000)

ctx.keymap({
    '(copy | stoosh)': Key('cmd-c'),
    '(paste | spark)': Key('cmd-v'),
    '(cut | snatch)': Key('cmd-x'),
    'allspark': Key('cmd-a cmd-v'),
    'allcopy': Key('cmd-a cmd-c'),
    'do park': [double_click, Key('cmd-v')],
    'do koosh': [double_click, Key('cmd-c')],

})
