import platform

import sublime_plugin
import sublime

COFFEE_COMMAND = 'coffee.cmd' if platform.system() == 'Windows' else 'coffee'


class CoffeeCompileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        text = self._get_text_to_compile()
        window = self.view.window()

        panel = window.get_output_panel("exec")
        panel.set_syntax_file('Packages/JavaScript/JavaScript.tmLanguage')

        window.run_command('exec', {
            'cmd': [COFFEE_COMMAND, '--print', '--lint', '--eval', text],
            'quiet': True
        })

    def _get_text_to_compile(self):
        region = self._get_selected_region() if self._editor_contains_selected_text() \
            else self._get_region_for_entire_file()
        return self.view.substr(region)

    def _get_region_for_entire_file(self):
        return sublime.Region(0, self.view.size())

    def _get_selected_region(self):
        return self.view.sel()[0]

    def _editor_contains_selected_text(self):
        for region in self.view.sel():
            if not region.empty():
                return True
        return False
