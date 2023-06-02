import PySimpleGUI as sg

def do_clipboard_event(event, window, element):
		if event == "Select All":
				element.Widget.selection_clear()
				element.Widget.tag_add('sel', '1.0', 'end')
		if event == "Copy":
				try:
						text = element.Widget.selection_get()
						window.TKroot.clipboard_clear()
						window.TKroot.clipboard_append(text)
				except:
						print("Nothing Selected!")
		if event == "Paste":
				element.Widget.insert(sg.tk.INSERT, window.TKroot.clipboard_get())
		if event == "Cut":
				try:
						text = element.Widget.selection_get()
						window.TKroot.clipboard_clear()
						window.TKroot.clipboard_append(text)
						element.update("")
				except:
						print("Nothing Selected!")

def redo(text):
	try:
		text.edit_redo()
	except:
		print("Nothing to Redo.")