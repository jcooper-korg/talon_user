# from https://github.com/talonvoice/examples
# jsc modified to wake dragon when talon sleeps, and v.v.

from talon.api import lib
from talon.voice import Context, ContextGroup, talon
from talon.engine import engine
from talon import app

def Mimic(phrase):
    engine.mimic(phrase.split())

def set_enabled(enable):
    if enable:
        talon.enable()
        Mimic('go to sleep')
        app.icon_color(0, 0.7, 0, 1)
    else:
        Mimic('wake up')
        talon.disable()
        app.icon_color(1, 0, 0, 1)
    lib.menu_check(b'!Enable Speech Recognition', enable)

def on_menu(item):
    if item == '!Enable Speech Recognition':
        set_enabled(not talon.enabled)

app.register('menu', on_menu)
set_enabled(talon.enabled)

sleep_group = ContextGroup('sleepy')
sleepy = Context('sleepy', group=sleep_group)

sleepy.keymap({
    'talon sleep': lambda m: set_enabled(False),
    'talon wake': lambda m: set_enabled(True),
})
sleep_group.load()
