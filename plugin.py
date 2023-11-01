# Copyright (C) 2023 Gerard Roche
#
# This file is part of Toggler.
#
# Toggler is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Toggler is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Toggler.  If not, see <https://www.gnu.org/licenses/>.

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
                    view.erase_status(preference_name.replace('show_', ''))

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
