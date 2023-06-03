# TextApp
Text Editor App Without All Of The Annoying Replit Files
Mostly compatible with windows.

---
## REQUIREMENTS ##
1. Python 3.11
2. PySimpleGUI (Python Module)
3. toml (Python Module)
4. AutoPep8 (Python Module)
5. All of the files included in the repo

---
## HOW TO INSTALL (STEP BY STEP) ##
1. Download the project as a zip file and then extract it
2. If not done already, install Python 3.11 (official site, or windows microsoft store)
3. If not done already, open the terminal/command prompt and type "pip install PySimpleGUI toml autopep8"
4. Place the extracted folder into the programs file (Or wherever comfortable)
5. Create a shortcut to the "TextApp" batch file
6. Place the shortcut on the desktop
7. Enjoy

---
## MY PROCESS ##
The first thing I did when I started this project was create a basic layout that I used to stylise and format the layout of the entire application. Starting on the application, I created a base class called "App" which I used as the parent for all of the applications windows. It holds the base dunder init and the base make_window function that is used to display the given layout on the window.

The next step in creation was to create the basic layout for the application. I did this by creating a new file called "default_layouts" this is used to avoid the reuse of already used layers, and it allows for the constant updating of the applications display. I implemented a class called MainApp to handle the functionality of the text editor portion of the app. That includes the folder/file browser, text editor box, line numbers, file functions and more.

I then created the "MainApp" class that both creates the layout for the main application and used the class to handle functionality such as line numbers, editor configuration, and repack widgets. Inside of the main loop, there are numerous conditionals checking for specific events. A majority of these events are used for file functionality, subprocessing and configuration editing.

There are multiple files, here is a brief description of all of them:

default_layouts: Creates and manages the default layouts of the application, used to reinitialise layouts due to PySimpleGUIs restrictions on reusing layouts. The layouts are defined in here and are assigned to specific classes with their functions. The function to get files for the file browser is also in this file.

clipboard_funcs: Defines the usage and functionality for functions such as copy, paste, cut and select all.

textEditor.bat: Runs the program through a batch file, create a shortcut to this file.

Themes: Stores and defines all theme elements created by users, initialises the themes created.

Config.toml: Defines the configuration for all of the application, the dimensions, version, user preferences and hidden file types.

---
## MY SUCCESS ##

I found my most success in the creation of the file functionality and layout creation of the application, here is a list of what I succeeded at:

1. Creating viable file systems for the use in saving and opening files.
2. The creation of a filetree system that reads through directories and files as long as they are not marked as "hidden" by the system.
3. The creation of easy to look at and easy to understand layouts.
4. A user preference system that allows users the change their theme, create new themes, alter the way lines wrap, the screen dimensions and the hidden file variables.
5. Clipboard functions.

---
## MY STRUGGLES ##

I mostly struggled with creating the line numbers and had to turn to the internet for that area. The main issues I had to work with were the file systems bugging out when I didnt want them to, the system crashing because some functionality was messy and didnt work, the organisation of my code, and especially the creation of the "Hidden File/Folder system" was especially difficult, because the creation of that resulted in me needing to rewrite the entire basis of the filetree system.

---
## WHAT I COULD DO BETTER ##

Thinking about problems on my own was one of the biggest struggles when it came to it. I feel that I could work on my problem solving capabilities a lot more and focus on using the internet less when it comes to solutions for problems. I feel I could do better at creating complex systems without help or solutions given to me, and think of those solutions on my own.

---
## Conclusion ##

Overall, this project was very easy, and I got very involved in the creation and maintaining of this application as it was an interesting task to undertake. It was far easier than I expected it to be, but nonetheless there were challenges I faced along the way. My initial proposal had far less features than I actually included in my project, and I am very glad I got to expand on the project as much as I could. This project may be updated for the future, so I hope I can continue to grab your attention.

---

### Final Project Commit (For School) Coming On June 9, 2023 ###
