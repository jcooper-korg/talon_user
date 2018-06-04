# from https://github.com/JonathanNickerson/talon_voice_user_scripts

from talon.voice import Context, Key

ctx = Context('editing')

ctx.keymap({
    'sage': Key('cmd-s'),
    'dizzle': Key('cmd-z'),
    'rizzle': Key('cmd-shift-z'),
    
})
