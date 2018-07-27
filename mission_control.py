# from https://github.com/JonathanNickerson/talon_voice_user_scripts

from talon.voice import Context, Key
from talon import macos

ctx = Context('mission_control')

ctx.keymap({
    "(mission control | troll up)": lambda m: macos.dock_notify('com.apple.expose.awake'),
    "(expozay | troll down)": lambda m: macos.dock_notify('com.apple.expose.front.awake'),		# jsc changed  'front' to 'exposay'
    "(next space | troll left)": Key('ctrl-alt-cmd-left'),
    "(last space | troll right)": Key('ctrl-alt-cmd-right'),
    "launchpad": lambda m: macos.dock_notify('com.apple.launchpad.toggle'),
    "show desktop": lambda m: macos.dock_notify('com.apple.showdesktop.awake'),
})
