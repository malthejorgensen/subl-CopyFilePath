import os

import sublime
import sublime_plugin

# Credits:
# - https://forum.sublimetext.com/t/file-name-and-full-path-to-clipboard/4833/9
# - https://stackoverflow.com/a/42633058
# - https://github.com/titoBouzout/SideBarEnhancements


class FilenameToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard(os.path.basename(self.view.file_name()))


class PathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard(self.view.file_name())
