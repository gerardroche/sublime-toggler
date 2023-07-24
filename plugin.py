from contextlib import contextmanager

from sublime import load_settings
from sublime import save_settings
from sublime import status_message
from sublime import windows
import sublime_plugin


class Toggler(sublime_plugin.WindowCommand):

    def run(self, setting=None, **kwargs):
        self.setting = setting

        on = kwargs.get('on') if 'on' in kwargs else True
        off = kwargs.get('off') if 'off' in kwargs else False

        with save_preferences() as preferences:
            preference_name = setting if setting else self.setting

            value = self.get_on_value_or(on)
            if preferences.get(preference_name) == value:
                value = self.get_off_value_or(off)

            preferences.set(preference_name, value)

            for window in windows():
                for view in window.views():
                    view.settings().erase(preference_name)

        status_message('{} is {}'.format(
            self.setting.replace('_', ' ').title(),
            'enabled' if value == self.get_on_value_or(on) else 'disabled'
        ))

    def get_off_value_or(self, default):
        return self.get_setting('%s_toggle_off' % self.setting, default)

    def get_on_value_or(self, default):
        return self.get_setting('%s_toggle_on' % self.setting, default)

    def get_setting(self, name: str, default=None):
        view = self.window.active_view()
        if view:
            value = view.settings().get(name)
            if value:
                return value

        if default is not None:
            return default


@contextmanager
def save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')
