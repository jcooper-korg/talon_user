# from https://github.com/talonvoice/examples
# jsc added my app shortcuts

from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui

apps = {}

def switch_app(m, name=None):		# jsc modified
    if name is None:
        name = str(m._words[1])
    full = apps.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            break


ctx = Context('switcher')
keymap = {
    'focus {switcher.apps}': switch_app,
    # jsc additions:
    'cody': lambda x: switch_app(x, "Xcode"),
    'maylap': lambda x: switch_app(x, "Mail"),
    'chromie': lambda x: switch_app(x, "Safari"),
    'smarty': lambda x: switch_app(x, "SmartGit"),
	'turmit': lambda x: switch_app(x, "Terminal"),
	'faindor': lambda x: switch_app(x, "Finder"),
	'slacker': lambda x: switch_app(x, "Slack"),
}
ctx.keymap(keymap)

def update_lists():
    global apps
    new = {}
    for app in ui.apps():
        words = app.name.split(' ')
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    if set(new.keys()) == set(apps.keys()):
        return
    ctx.set_list('apps', new.keys())
    apps = new


def ui_event(event, arg):
    if event in ('app_activate', 'app_deactivate', 'app_launch', 'app_close'):
        update_lists()


ui.register('', ui_event)
update_lists()
