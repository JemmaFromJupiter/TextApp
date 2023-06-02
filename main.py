from __future__ import annotations
import PySimpleGUI as sg
# from colours import *
import os
import themes
import defaultLayouts
import clipboard_funcs
import autopep8
import webbrowser
import toml as tmlb

"""Text Editor 1.0"""

themes.init_themes()

config = tmlb.load(f"{os.getcwd()}/config.toml")


class App():

	def __init__(self, title: str, theme: str = None):
		self.title = title
		self.window_dims = list(
			config["client"]["client_dimensions"].split("x"))
		self.theme = theme

	def make_window(self, layout, **kwargs):
		self.window_dims = list(
			config["client"]["client_dimensions"].split("x"))
		layout_ = layout
		return sg.Window(self.title, layout_, size=self.window_dims, **kwargs)


class fileFunctions():
	def __init__(self):
		pass

	def saveFile(self, file, file_contents):
		if file is not None:
			with open(file, "w") as f:
				f.write(file_contents.get())
		else:
			saved_file = self.saveFileAs(file_contents)
			if saved_file:
				return saved_file

	def saveFileAs(self, file_contents):
		new_file = sg.popup_get_file("Save As...", save_as=True)
		if new_file is not None and not os.path.isfile(new_file):
			with open(new_file, "x") as f:
				f.write(file_contents.get())
				return new_file
		elif new_file is not None and os.path.isfile(new_file):
			with open(new_file, "w") as f:
				f.write(file_contents.get())
				return new_file

	def openFile(self, editBox):
		file_opened = sg.popup_get_file("Select File To Open...")
		if file_opened is not None:
			with open(file_opened, "r") as f:
				editBox.update(value=f.read())
				return file_opened

	def deleteFile(self, fileName):
		if len(fileName) == 1:
			if os.path.exists(fileName[0]):
				print(fileName[0])
				os.remove(fileName[0])
			else:
				print("File Does Not Exist!")
		else:
			for i in range(len(fileName)):
				print(fileName[i])
				if os.path.exists(fileName[i]):
					os.remove(fileName[i])
				else:
					print("Path Does Not Exist!")


class Terminal(App):
	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.window = self.make_window(defaultLayouts.makeTerminal_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)

	def mainloop(self):
		while True:
			event, values = self.window.read()
			if event in (sg.WINDOW_CLOSED, "EXIT"):
				self.window.close()
				break
			if event == "RUN":
				try:
					cmd_list = values["-TerminalInput-"].split(" ")
					sp = sg.execute_command_subprocess(
						cmd_list[0], *cmd_list[1:], pipe_output=True, wait=False)
					results = sg.execute_get_results(sp, timeout=1)
					print(results[0])
				except Exception as err:
					print(err)


class About(App):
	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.window = self.make_window(defaultLayouts.makeAbout_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)

	def mainloop(self):
		while True:
			event, values = self.window.read()
			if event == sg.WINDOW_CLOSED:
				break


class Console(App):
	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.window = self.make_window(defaultLayouts.makeConsole_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)

	def mainloop(self):
		while True:
			event, values = self.window.read()
			if event == sg.WINDOW_CLOSED:
				break


class ThemeCreator(App):

	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.layout = None
		self.window = self.make_window(defaultLayouts.makeTheme_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)

	def mainloop(self):
		while True:
			event, values = self.window.read()
			print(event, values)
			if event in [sg.WINDOW_CLOSED, "Exit"]:
				break
			if event == '-BGCOL-':
				self.window["-BGCOL_-"].update(
					background_color=values["-BGCOL-"])
			if event == '-TXTCOL-':
				self.window["-TXTCOL_-"].update(
					background_color=values["-TXTCOL-"])
			if event == '-INCOL-':
				self.window["-INCOL_-"].update(
					background_color=values["-INCOL-"])
			if event == '-TXINCOL-':
				self.window["-TXINCOL_-"].update(
					background_color=values["-TXINCOL-"])
			if event == '-SCRLCOL-':
				self.window["-SCRLCOL_-"].update(
					background_color=values["-SCRLCOL-"])
			if event == "-BTNCOL-":
				self.window["-BTNCOL1_-"].update(
					background_color=values["-BTNCOL-"])
			if event == "-BTNCOL2-":
				self.window["-BTNCOL2_-"].update(
					background_color=values["-BTNCOL2-"])
			if event == "-PRGCOL-":
				self.window["-PRGCOL1_-"].update(
					background_color=values["-PRGCOL-"])
			if event == "-PRGCOL2-":
				self.window["-PRGCOL2_-"].update(
					background_color=values["-PRGCOL2-"])
			if event == "-THCREATESIMPSUBMIT-":
				themes.theme_dicts.append(
					{
						'NAME': values["-THNM-"],
						'BACKGROUND': values["-BGCOL-"],
						'TEXT': values['-TXTCOL-'],
						'INPUT': values['-INCOL-'],
						'TEXT_INPUT': values['-TXINCOL-'],
						'SCROLL': values['-SCRLCOL-'],
						'BUTTON': (values['-BTNCOL-'], values['-BTNCOL2-']),
						'PROGRESS': (values['-PRGCOL-'], values['-PRGCOL2-']),
						'BORDER': values['-BWID-'],
						'SLIDER_DEPTH': values['-SLDEP-'],
						'PROGRESS_DEPTH': values['-PRGDEP-']
					}
				)
				with open("themes/theme_store.py", "w") as f:
					f.write(f"theme_dicts = {themes.theme_dicts}")
				self.window.close()
				break
			if event == "-THCREATEADVSUBMIT-":
				myDict = eval(self.window["-ADVLOBOX-"].get())
				themes.theme_dicts.append(
					myDict
				)
				with open("themes/theme_store.py", "w") as f:
					f.write(f"theme_dicts = {themes.theme_dicts}")
				self.window.close()
				break


class themeSelector(App):
	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.window = self.make_window(defaultLayouts.makeTh_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)

	def mainloop(self):
		while True:
			event, values = self.window.read()
			print(event, values)
			if event in (sg.WINDOW_CLOSED, "Cancel"):
				self.window.close()
				break
			elif event == "-THSELECTSUBMIT-":
				self.window.close()
				return values["-SELTHEME-"][0]


class userPrefs(App):
	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.window = self.make_window(defaultLayouts.makeUserPrefs_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)

	def save_client_preferences(self):
		with open(f"{os.getcwd()}/config.toml", "wb") as up:
			up.seek(0)
			up.write(bytes(tmlb.dumps(config).encode("utf-8")))
			up.truncate()
			up.close()

	def mainloop(self):
		while True:
			event, values = self.window.read()
			print(event, values)
			if event in (sg.WINDOW_CLOSED, "Cancel"):
				self.window.close()
				return False
			if event == "-C_HIDE_ADD-":
				if values["-C_HIDE_ADD_-"] not in self.window["-C_HIDE-"].get_list_values():
					self.window["-C_HIDE-"].update(
						values=self.window["-C_HIDE-"].get_list_values() + [values["-C_HIDE_ADD_-"]])
					self.window["-C_HIDE_ADD_-"].update(value="")
			if event == "-C_HIDE_REMOVE-":
				try:
					ls = list(self.window["-C_HIDE-"].get_list_values())
					ls.remove(values["-C_HIDE-"][0])
					self.window["-C_HIDE-"].update(values=ls)
				except:
					print("H")
			if event == "Save":
				config["user"]["linewrap"] = values["-LWPREF-"]
				if values["-THPREF-"]:
					config["user"]["theme"] = values["-THPREF-"][0]
				if values["-DIMSS-"]:
					config["client"]["client_dimensions"] = values["-DIMSS-"]
				config["client"]["client_hidden"] = self.window["-C_HIDE-"].get_list_values()
				self.save_client_preferences()
				self.window.close()
				return True


class MainApp(App):

	def __init__(self, title: str, theme: str = None):
		super().__init__(title, theme)
		self.fileFuncs = fileFunctions()
		self.currentFileName = None
		self.file_extension = None
		self.console = None
		self.terminal = None
		self.prefs = None
		self.creThme = None
		self.about = None
		self.right_click_menu = ["", ["Copy", "Paste", "Cut", "Select All"]]
		self.window = self.make_window(defaultLayouts.makeMain_layout(
			self.window_dims, self.theme), resizable=True, finalize=True)
		self.text = self.window['-EDITBOX-'].Widget
		self.text.configure(undo=True)
		self.configure_lineNums()

	def create_window_bindings(self):
		self.window.bind("<Control_L><a>", "Select All")
		self.window.bind('<Control_L><Shift_L><Z>',
						 lambda text=self.text: clipboard_funcs.redo(text))
		self.window.bind('<Control_L><o>', "Open File")
		self.window.bind('<Control_L><s>', "Save File")
		self.window.bind('<Control_L><Shift_L><S>', "Save As")
		self.window.bind('<Control_L><Shift_L><R>', "Run Code", False)
		print(self.window.TKroot)

	def configure_lineNums(self):
		if self.window is not None:
			self.m1, self.m2 = self.window['line_nums'], self.window['-EDITBOX-']
			self.repack(self.m1.widget, {'fill': 'y', 'expand': False})
			self.repack(self.m1.widget.master, {
						'fill': 'y', 'expand': False, 'before': self.m2.widget.master})
			self.m1.widget.bindtags(
				(str(self.m1.widget), str(self.window.TKroot), "all"))
			self.m2.bind('<Configure>', '')
			self.m2.bind('<MouseWheel>', '')
			self.ratio, self.lines = 0, 0
			self.configureTextEditSettings()
			self.create_window_bindings()

	def configureTextEditSettings(self):
		self.m2.widget.config(wrap=config["user"]["linewrap"])
		self.window.refresh()

	def repack(self, widget, option):
		pack_info = widget.pack_info()
		pack_info.update(option)
		widget.pack(**pack_info)

	def mainloop(self):
		while True:
			try:
				event, values = self.window.read()
				print(event, values)
				if event in (sg.WIN_CLOSED, "Exit"):
					self.window.close()
					self.window = None
					if self.console is not None:
						self.console.window.close()
					if self.terminal is not None:
						self.terminal.window.close()
					if self.prefs is not None:
						self.prefs.window.close()
					if self.creThme is not None:
						self.creThme.window.close()
					if self.about is not None:
						self.about.window.close()
					break
				if event == "New File":
					self.fileFuncs.saveFile(
						self.currentFileName, self.window["-EDITBOX-"])
					self.window['-EDITBOX-'].update(value="")
					self.currentFileName = None
					self.window.set_title("Text Editor 0.0.3")
				if event == "Open File":
					file_opened = self.fileFuncs.openFile(
						self.window["-EDITBOX-"])
					if file_opened:
						self.currentFileName = file_opened
						self.file_extension = self.currentFileName.split(".")[
							1]
						self.window.set_title(self.currentFileName)
				if event == "Save File":
					saved_file = self.fileFuncs.saveFile(
						self.currentFileName, self.window["-EDITBOX-"])
					if saved_file:
						self.currentFileName = saved_file
						self.file_extension = self.currentFileName.split(".")[
							1]
						self.window.set_title(self.currentFileName)
				if event == "Save As":
					saved_file = self.fileFuncs.saveFileAs(
						self.window["-EDITBOX-"])
					if saved_file:
						self.currentFileName = saved_file
						self.file_extension = self.currentFileName.split(".")[
							1]
						self.window_dims = self.window.size
						self.editboxValue = self.window["-EDITBOX-"].get()
						self.window_location = self.window.current_location()
						self.window.close()
						self.window = self.make_window(defaultLayouts.makeMain_layout(
							self.window_dims, self.theme), resizable=True, finalize=True)
						self.window.set_title(self.currentFileName)
				if event == "Run Code":
					if self.currentFileName is not None:
						saved_file = self.fileFuncs.saveFile(
							self.currentFileName, self.window["-EDITBOX-"])
						if saved_file:
							self.currentFileName = saved_file
							self.file_extension = self.currentFileName.split(".")[
								1]
							self.window.set_title(self.currentFileName)
						self.console = Console("Console", theme=self.theme)
						self.console.window["-OUTPUT-"].update(disabled=True)
						cmd = ""
						if self.file_extension == "py":
							cmd = "python3"
						print(self.currentFileName)
						sp = sg.execute_command_subprocess(
							cmd, str(self.currentFileName), pipe_output=True, wait=False)
						results = sg.execute_get_results(sp, timeout=1)
						print(results[0])
						self.console.mainloop()
					else:
						sg.popup_error("File is Empty or Non-Existant!")
				if event == "-FOLDERTREE-":
					try:
						self.window["-EDITBOX-"].update(value=open(
							values["-FOLDERTREE-"][0], "r").read())
						self.currentFileName = values["-FOLDERTREE-"][0]
						self.file_extension = self.currentFileName.split(".")[
							1]
						self.window.set_title(self.currentFileName)
					except:
						print("Could not do that!")
				if event == "Choose Theme":
					self.themeSelector = themeSelector(
						"Select Theme", self.theme)
					selected_theme = self.themeSelector.mainloop()
					if selected_theme:
						self.theme = selected_theme
						self.window_dims = self.window.size
						self.editboxValue = self.window["-EDITBOX-"].get()
						self.window_location = self.window.current_location()
						self.window.close()
						self.window = self.make_window(defaultLayouts.makeMain_layout(
							self.window_dims, self.theme), resizable=True, finalize=True, location=self.window_location)
						self.window["-EDITBOX-"].update(
							value=self.editboxValue)
				if event == "Delete File":
					self.fileFuncs.deleteFile(values['-FOLDERTREE-'])
					self.window['-FOLDERTREE-'].update(values=sg.TreeData())
					self.window_dims = self.window.size
					self.window.close()
					self.window = self.make_window(defaultLayouts.makeMain_layout(
						self.window_dims, self.theme), resizable=True, finalize=True)
				if event in self.right_click_menu[1]:
					clipboard_funcs.do_clipboard_event(
						event, self.window, self.window["-EDITBOX-"])
				if event == "Redo":
					clipboard_funcs.redo(self.text)
				if event == "About...":
					self.window_dims = self.window.size
					self.about = About("About", self.theme)
					self.about.mainloop()
				if event == "Create Theme":
					self.window_dims = self.window.size
					self.creThme = ThemeCreator("Theme Creator", self.theme)
					self.creThme.mainloop()
					themes.init_themes()
				if event == "Format Code":
					try:
						autopep8.fix_file(self.currentFileName)
						self.window["-EDITBOX-"].update(
							value=open(self.currentFileName, "r").read())
					except:
						sg.popup_error("Could Not Format File",
									   title="Format Error", modal=False)
				if event == "Terminal":
					self.terminal = Terminal("Terminal Window", self.theme)
					self.terminal.mainloop()
				if event in ('-EDITBOX-', "Open File", "-FOLDERTREE-"):
					self.window.refresh()
					new_ratio, _ = self.m2.vsb.get()
					new_lines = int(self.m2.widget.index(
						sg.tk.END).split('.')[0]) - 1
					if new_lines != self.lines:
						self.lines = new_lines
						text = '\n'.join(
							[f'{i+1} ' for i in range(self.lines)])
						current = int(self.m2.widget.index(
							sg.tk.INSERT).split('.')[0])
						self.m1.update(text)
					if new_ratio != self.ratio:
						self.ratio = new_ratio
						self.m1.set_vscroll_position(
							self.ratio+(self.ratio//2))
				if event == "Preferences":
					self.prefs = userPrefs("Preferences", self.theme)
					saved = self.prefs.mainloop()
					if saved:
						self.theme = config["user"]["theme"]
						self.window.close()
						self.window = self.make_window(defaultLayouts.makeMain_layout(
							self.window_dims, self.theme), resizable=True, finalize=True)
				if event == "dirnm":
					config["user"]["browsing_dir"] = values["dirnm"]
					self.prefs = userPrefs("Preferences", self.theme)
					self.prefs.save_client_preferences()
					self.prefs.window.close()
					self.window.close()
					self.window = self.make_window(defaultLayouts.makeMain_layout(
						self.window_dims, self.theme), resizable=True, finalize=True)
				if event == "git":
					webbrowser.open(values['git'])
					
				if self.window is not None:
					self.configure_lineNums()
			except Exception as err:
				raise Exception(
					"Unexpected Error Occurred: ", err)


appWin = MainApp(
	f"{config['client']['client_name']} {config['client']['client_version']}", config["user"]["theme"])
appWin.mainloop()