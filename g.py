######## Function Holder for all Constant Global Variables ########
app_name = "Visual Py Builder 1.0"


####### Program Settings #######
dbg = False  ## SET TRUE FOR DEBUGGING PURPOSES
# serverurl = "http://localhost/myserver/"
serverurl = "http://localhost:8083/"


######## GUI Variables ########
defaultPage = "pg_main"
fullScreen = False
frameWidth = 800
frameHeight = 480
bgColor = "#00aeff"
bgColorBlack = "#000000"
cursor = True 
scrollWidth = 35


####### Keyboard Variables ########
useKeyboard = True
kbshift = False
kbpage = ""
kbelement = ""
kbcurstring = ""
kbpassword = False

####### Keyboard Settings ########    
kbwadj = 4 ## HORIZONTAL MARGIN BETWEEN BUTTONS
kbhadj = 4 ## VERTICAL MARGIN BETWEEN BUTTONS


####### System Settings #######

from sys import platform
if (platform == "linux") or (platform == "linux2") : os = "linux"
elif platform == "darwin": os = "mac"
elif platform == "win32": os = "win"


#_____ BUILDER SETTINGS _____#
builder_title = "Visual"
builder_title_sub = "Py Builder 1.0"
builder_font = "isometric4"
defaultMessageBoxTitle = app_name
#_____ BUILDER SETTINGS _____#



####### System Settings #######
