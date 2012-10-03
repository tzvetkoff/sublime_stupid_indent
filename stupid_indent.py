#!/usr/bin/env python
# coding: utf8

import os.path
import fnmatch
import sublime
import sublime_plugin

class StupidIndent(sublime_plugin.EventListener):
	def on_load(self, view):
		n = os.path.basename(view.file_name());
		s = view.settings()
		c = s.get('stupid_indent', [])
		for v in c:
			for p in v.get('patterns', []):
				if fnmatch.fnmatch(n, p):
					s.set('tab_size', v.get('tab_size', s.get('tab_size')))
					s.set('translate_tabs_to_spaces', v.get('translate_tabs_to_spaces', s.get('translate_tabs_to_spaces')))
					return
