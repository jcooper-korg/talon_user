# Talon voice commands for google drive
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Context, Key, press
from talon import ctrl

ctx = Context('google_drive', func=lambda app, win:
              win.title.endswith('- Google Drive') or '- Google Drive -' in win.title)
ctx.keymap({
    'rename': Key('n'),
    'open': Key('enter'),
    'move': Key('z'),
})
