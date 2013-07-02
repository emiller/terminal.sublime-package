"""
@author       emiller
@date         01/22/2013
@description  Simple Sublime plugin that enables the familiar
              Open Terminal Here support within the editor.
"""

import sublime, sublime_plugin, os, sys

class OpenTerminalCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    path = os.path.dirname(self.view.file_name())

    if not os.path.exists(path):
      sublime.error_message('Hmm, that path doesn\'t exist anymore.')
      return

    platform = sys.platform.lower()
    terminal = None

    if platform.startswith('linux'):
      terminal = 'cd %s; x-terminal-emulator' % path

    elif platform.startswith('osx') or platform.startswith('darwin'):
      terminal = 'open -a Terminal %s' % path

    if terminal is None:
      sublime.message_dialog('Sorry, only Linux and OSX are supported currently.') 
      return

    try:
      os.system(terminal)

    except Exception, e:
      sublime.error_message('Unable to open terminal (%s) because: %s' % (terminal, str(e)))

