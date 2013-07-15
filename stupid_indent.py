#!/usr/bin/env python
# coding: utf8

import os.path
import fnmatch
import sublime
import sublime_plugin

class StupidIndent(sublime_plugin.EventListener):
	def on_load(self, view):
		basename = os.path.basename(view.file_name());
		settings = view.settings()

		for entry in sublime.load_settings('Stupid Indent.sublime-settings').get('configuration'):
			for pattern in entry.get('patterns', []):
				if fnmatch.fnmatch(basename, pattern):
					settings.set('tab_size', entry.get('tab_size', settings.get('tab_size')))
					settings.set('translate_tabs_to_spaces', entry.get('translate_tabs_to_spaces', settings.get('translate_tabs_to_spaces')))
					return
