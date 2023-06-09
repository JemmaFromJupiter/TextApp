from __future__ import annotations
import PySimpleGUI as sg
import os
import sys
import time
import toml as tmlb

lin_dar = ["linux", "darwin"]

win = ["win32", "cygwin"]

class Platform:
    def __init__(self):
        self._name = sys.platform
        self._version = sys.version_info

    def get_sys_str_fmt(self):
        if self._name in lin_dar:
            return "/"
        if self._name in win:
            return "\\"


platform = Platform()

config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")

print(sys.platform)
sys.setrecursionlimit(10000)

folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

default_theme = """{
    'NAME': '',
    'BACKGROUND': '',
    'TEXT': '',
    'INPUT': '',
    'TEXT_INPUT': '',
    'SCROLL': '',
    'BUTTON': ('', ''),
    'PROGRESS': ('', ''),
    'BORDER': '',
    'SLIDER_DEPTH': '',
    'PROGRESS_DEPTH': ''
}"""


def get_dir_contents(parent, dirname, treedata):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname, f)
        splt_fullname = fullname.split(platform.get_sys_str_fmt())
        idx = 0
        for _ in splt_fullname:
            idx += 1
            if _ not in config["client"]["client_hidden"] and idx == len(splt_fullname):
                if "." in _:
                    _ = _.split(".")
                    if _[-1] not in config["client"]["client_hidden"]:
                        treedata.Insert(parent, fullname, f, values=[
                                        os.stat(fullname).st_size], icon=file_icon)
                        break
                    else:
                        continue
                if os.path.isdir(fullname):
                    treedata.Insert(parent, fullname, f,
                                    values=[], icon=folder_icon)
                    get_dir_contents(fullname, fullname, treedata)
                else:
                    treedata.Insert(parent, fullname, f, values=[
                                    os.stat(fullname).st_size], icon=file_icon)
                idx = 0
                break
    return treedata


def makeAbout_layout(dims: tuple[int], theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)

    info_tab = [
        [sg.Text(f"""
Owner: {config["owner"]["name"]}

{config['client']['description']['desc']}

Links:
""")],
	[
        sg.Text("Github: "), sg.Text(f"{config['owner']['git_link']}", enable_events=True, k="git")
	]
    ]

    keyBinds_tab = [
        [sg.Text("Open File      Ctrl-o", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Save File      Ctrl-s", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Save As        Ctrl-Shift-S", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Undo           Ctrl-z", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Redo           Ctrl-Shift-Z", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Copy           Ctrl-c", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Paste          Ctrl-v", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Cut            Ctrl-x", expand_x=True,
                 expand_y=True, justification="center")],
        [sg.Text("Select All     Ctrl-a", expand_x=True,
                 expand_y=True, justification="center")],
    ]

    tabA, tabB = sg.Tab("Information", info_tab), sg.Tab(
        "Key Binds", keyBinds_tab)

    layout = [
        [sg.TabGroup([[tabA, tabB]], expand_x=True, expand_y=True)]
    ]
    return layout


def makeTerminal_layout(dims: tuple, theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)
    layout = [
        [sg.Multiline(autoscroll=True, expand_x=True, expand_y=True, k="-TerminalOutput-", echo_stdout_stderr=True,
                      reroute_cprint=True, reroute_stdout=True, reroute_stderr=True, write_only=True)],
        [sg.Input(k="-TerminalInput-", expand_x=True), sg.Button("RUN",
                                                                 expand_x=True, bind_return_key=True), sg.Button("EXIT", expand_x=True)]
    ]
    return layout


def makeConsole_layout(dims: tuple[int], theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)
    layout = [
        [sg.Multiline(size=dims, autoscroll=True, expand_x=True, expand_y=True,
                      reroute_stdout=True, echo_stdout_stderr=True, write_only=True, k="-OUTPUT-")]
    ]
    return layout


def makeTh_layout(dims: tuple[int], theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)
    layout = [
        [sg.Listbox(sg.theme_list(), expand_x=True, expand_y=True,
                    enable_events=True, k="-SELTHEME-")],
        [sg.Button("Confirm", k="-THSELECTSUBMIT-", expand_x=True),
         sg.Button("Cancel", expand_x=True)]
    ]
    return layout


def makeTheme_layout(dims: tuple[int], theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)

    simpleTXTCol = [
        [sg.Text("Theme Name: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Background: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Text Color: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Input Color: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Input Text Color: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Scroll Color: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Button Color: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Progress Bar Color: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Border Width: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Slider Depth: ")],
        [sg.Sizer(0, 5)],
        [sg.Text("Progress Depth: ")],
        [sg.Sizer(0, 5)],
    ]

    inputsCol = [
        [sg.Input(size=(15, 1), k="-THNM-")],
        [sg.Input(size=(2, 1), k="-BGCOL_-"), sg.Input(visible=False, enable_events=True,
                                                       k="-BGCOL-"), sg.ColorChooserButton("Pick Colour", k="-BGPICK-")],
        [sg.Input(size=(2, 1), k="-TXTCOL_-"), sg.Input(visible=False, enable_events=True,
                                                        k="-TXTCOL-"), sg.ColorChooserButton("Pick Colour", k="-TXTPICK-")],
        [sg.Input(size=(2, 1), k="-INCOL_-"), sg.Input(visible=False, enable_events=True,
                                                       k="-INCOL-"), sg.ColorChooserButton("Pick Colour", k="-INPICK-")],
        [sg.Input(size=(2, 1), k="-TXINCOL_-"), sg.Input(visible=False, enable_events=True,
                                                         k="-TXINCOL-"), sg.ColorChooserButton("Pick Colour", k="-TXINPICK-")],
        [sg.Input(size=(2, 1), k="-SCRLCOL_-"), sg.Input(visible=False, enable_events=True,
                                                         k="-SCRLCOL-"), sg.ColorChooserButton("Pick Colour", k="-SCRLPICK-")],
        [sg.Input(size=(2, 1), k="-BTNCOL1_-"), sg.Input(visible=False, enable_events=True, k="-BTNCOL-"), sg.ColorChooserButton("Pick Colour", k="-BTNPICK-"),
         sg.Input(size=(2, 1), k="-BTNCOL2_-"), sg.Input(visible=False, enable_events=True, k="-BTNCOL2-"), sg.ColorChooserButton("Pick Colour", k="-BTNPICK2-")],
        [sg.Input(size=(2, 1), k="-PRGCOL1_-"), sg.Input(visible=False, enable_events=True, k="-PRGCOL-"), sg.ColorChooserButton("Pick Colour", k="-PRGPICK-"),
         sg.Input(size=(2, 1), k="-PRGCOL2_-"), sg.Input(visible=False, enable_events=True, k="-PRGCOL2-"), sg.ColorChooserButton("Pick Colour", k="-PRGPICK2-")],
        [sg.Input(size=(1, 1), k="-BWID-")],
        [sg.Input(size=(1, 1), k="-SLDEP-")],
        [sg.Input(size=(1, 1), k="-PRGDEP-")]
    ]

    Simple_layout = [
        [sg.Col(simpleTXTCol, expand_x=True, expand_y=True),
         sg.Col(inputsCol, expand_x=True, expand_y=True)],
        [sg.Button("Submit", k='-THCREATESIMPSUBMIT-')]
    ]
    Adv_layout = [
        [sg.Multiline(default_text=default_theme, expand_x=True,
                      expand_y=True, k="-ADVLOBOX-")],
        [sg.Button("Submit", k="-THCREATEADVSUBMIT-")]
    ]
    ThemeCreator_layout = [
        [sg.Frame("Simple Formatting", Simple_layout, expand_x=True, expand_y=True), sg.Frame(
            "Advanced Formatting", Adv_layout, expand_x=True, expand_y=True)],
    ]
    return ThemeCreator_layout


def makeUserPrefs_layout(dims: tuple[int], theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)
    layout = [
        [sg.Text("LineWrap: ")],
        [sg.Combo(["word", "none"], expand_x=True, default_value=config["user"]
                  ["linewrap"], k="-LWPREF-", readonly=True)],
        [sg.Text("Screen Dimensions: ")],
        [sg.Combo(["1920x1080", "1280x720", "854x480", "640x360", "426x240"], default_value=config["client"]
                  ["client_dimensions"], expand_x=True, readonly=True, k="-DIMSS-")],
        [sg.Text("Theme: ")],
        [sg.Input(expand_x=True, enable_events=True, k="-TH_SEARCH-")],
        [sg.Listbox(sg.theme_list(), expand_x=True,
                    expand_y=True, k="-THPREF-")],
        [sg.Text("Hidden Files:")],
        [sg.Listbox(config["client"]["client_hidden"],
                    k="-C_HIDE-", expand_x=True, expand_y=True)],
        [sg.Col([[sg.Input(k="-C_HIDE_ADD_-"), sg.Button("+", size=(2, 1), k="-C_HIDE_ADD-"),
                  sg.Button("-", size=(2, 1), k="-C_HIDE_REMOVE-")]], justification="right")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    return layout


def makeMain_layout(dims: tuple[int], theme: str):
    config = tmlb.load(f"{os.getcwd()}{platform.get_sys_str_fmt()}config.toml")
    if theme:
        sg.theme(theme)
    MenuBar_layout = [
        ['&File', ['&New File', '&Open File', '&Save File', "&Save As",
                   '&Properties', ['&Create Theme', "&Preferences"], 'E&xit']],
        ['&Edit', ['&Copy', '&Paste', '!&Undo', '&Redo']],
        ['&Tools', ['&Run Code', '&Format Code', "&Terminal"]],
        ['&Help', ['&About...']]
    ]

    if config["user"]["browsing_dir"] == "current":
        fileBrowse_layout = sg.Col([[sg.Text("Select Directory to Browse", expand_x=True), sg.Input(enable_events=True, visible=False, k="dirnm"), sg.FolderBrowse(enable_events=True, k="dirnm_")], [sg.Tree(
            get_dir_contents("", os.getcwd(), sg.TreeData()), vertical_scroll_only=False, expand_x=True, expand_y=True, k="-FOLDERTREE-", headings=["Size", ], enable_events=True, right_click_menu=["", ["Delete File"]])]])
    else:
        fileBrowse_layout = sg.Col([[sg.Text("Select Directory to Browse", expand_x=True), sg.Input(enable_events=True, visible=False, k="dirnm"), sg.FolderBrowse(enable_events=True, k="dirnm_")], [sg.Tree(get_dir_contents(
            "", config["user"]["browsing_dir"], sg.TreeData()), vertical_scroll_only=False, expand_x=True, expand_y=True, k="-FOLDERTREE-", headings=["Size", ], enable_events=True, right_click_menu=["", ["Delete File"]])]])
    editor_layout = sg.Col([
        [
            sg.Multiline(size=(3, dims[1]), pad=(0, 0), justification="right", expand_x=True,
                         expand_y=True, k="line_nums", write_only=True, no_scrollbar=True),
            sg.Multiline(size=dims, pad=(0, 0), horizontal_scroll=True, sbar_width=3, sbar_arrow_width=3, justification="left", expand_x=True,
                         expand_y=True, k="-EDITBOX-", enable_events=True, focus=True, right_click_menu=["", ["Copy", "Paste", "Cut", "Select All"]])
        ]])

    MainWindow_layout = [
        [sg.Menu(MenuBar_layout)],
        [sg.Pane([fileBrowse_layout, editor_layout],
                 orientation="h", expand_x=True, expand_y=True)]
    ]
    return MainWindow_layout